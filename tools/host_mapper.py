import concurrent.futures
import ipaddress
import os
import random
import select
import socket
import struct
import threading
import time

ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY = 0
ICMP_HEADER_FORMAT = "!BBHHH"
ICMP_HEADER_SIZE = struct.calcsize(ICMP_HEADER_FORMAT)
PING_TIMEOUT = 4
output_lock = threading.Lock()


def _checksum(data):
    if len(data) % 2:
        data += b"\x00"

    total = 0
    for index in range(0, len(data), 2):
        total += (data[index] << 8) + data[index + 1]
        total = (total & 0xFFFF) + (total >> 16)

    return (~total) & 0xFFFF


def _build_echo_request(identifier, sequence):
    timestamp = struct.pack("!d", time.time())
    payload = timestamp + os.urandom(40)
    header = struct.pack(ICMP_HEADER_FORMAT, ICMP_ECHO_REQUEST, 0, 0, identifier, sequence)
    checksum = _checksum(header + payload)
    header = struct.pack(ICMP_HEADER_FORMAT, ICMP_ECHO_REQUEST, 0, checksum, identifier, sequence)
    return header + payload


def _parse_echo_reply(packet, identifier, sequence):
    if len(packet) < 20 + ICMP_HEADER_SIZE:
        return None

    ip_header_length = (packet[0] & 0x0F) * 4
    icmp_packet = packet[ip_header_length:]
    if len(icmp_packet) < ICMP_HEADER_SIZE:
        return None

    icmp_type, _, _, reply_identifier, reply_sequence = struct.unpack(
        ICMP_HEADER_FORMAT, icmp_packet[:ICMP_HEADER_SIZE]
    )

    if icmp_type != ICMP_ECHO_REPLY:
        return None
    if reply_identifier != identifier or reply_sequence != sequence:
        return None

    payload = icmp_packet[ICMP_HEADER_SIZE:]
    if len(payload) < 8:
        return None

    sent_time = struct.unpack("!d", payload[:8])[0]
    return max(0.0, time.time() - sent_time)


def _ping_host(ip_str, timeout=PING_TIMEOUT):
    identifier = os.getpid() & 0xFFFF
    sequence = random.randint(0, 0xFFFF)
    packet = _build_echo_request(identifier, sequence)

    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
        sock.setblocking(False)
        sock.sendto(packet, (ip_str, 0))
        deadline = time.time() + timeout

        while True:
            remaining = deadline - time.time()
            if remaining <= 0:
                return None

            ready, _, _ = select.select([sock], [], [], remaining)
            if not ready:
                return None

            reply_packet, _ = sock.recvfrom(4096)
            delay = _parse_echo_reply(reply_packet, identifier, sequence)
            if delay is not None:
                return delay


def check_host(ip_str):
    try:
        response_time = _ping_host(ip_str)
        if response_time is not None:
            return f"{ip_str} is reachable (delay: {response_time:.4f}s)"
    except PermissionError:
        return "ICMP scanning requires elevated privileges"
    except OSError:
        pass


def run(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    hosts = [str(ip) for ip in network.hosts()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(check_host, hosts))

    privilege_error = any(result == "ICMP scanning requires elevated privileges" for result in results)
    up_hosts = [result for result in results if result and "reachable" in result]

    output = []
    if privilege_error:
        output.append("ICMP scanning requires elevated privileges")
    elif not up_hosts:
        output.append("No hosts are up")
    else:
        output.append("Live hosts found:")
        for result in up_hosts:
            output.append(result.split()[0])

    with output_lock:
        for line in output:
            print(line)

    return "\n".join(output)
