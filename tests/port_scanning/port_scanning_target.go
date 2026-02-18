package main

import (
	"fmt"
	"net"
	"time"
)

func startServer(port string, response string, delay time.Duration) {
	ln, err := net.Listen("tcp", ":"+port)
	if err != nil {
		panic(err)
	}
	fmt.Println("Listening on port", port)

	for {
		conn, err := ln.Accept()
		if err != nil {
			continue
		}

		go func(c net.Conn) {
			defer c.Close()
			time.Sleep(delay)
			c.Write([]byte(response))
		}(conn)
	}
}

func main() {
	go startServer("21", "220 FTP Service Ready\r\n", 0)
	go startServer("22", "SSH-2.0-OpenSSH_8.2\r\n", 0)
	go startServer("25", "220 SMTP Ready\r\n", 0)
	go startServer("80", "HTTP/1.1 200 OK\r\n\r\nHello", 0)
	go startServer("3306", "MySQL Server\n", 0)
	go startServer("9000", "Slow service PostgreSQL...\n", 3*time.Second) // simulate slow
	go startServer("1111", "HTTPS...\n", 0) // simulate slow


	select {}
}
