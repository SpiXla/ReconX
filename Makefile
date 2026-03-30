.PHONY: install run test test-go stop lint clean develop help setup

# Defaults
VENV        := venv
PYTHON      := $(VENV)/bin/python
PIP         := $(VENV)/bin/pip
GO          := go

# PID files
PS_PID_FILE   := ps.pid
FUZZ_PID_FILE := fuzz.pid

help:
	@echo "ReconX Makefile:"
	@echo "  make install  - Setup virtualenv"
	@echo "  make run      - Run main Python app"
	@echo "  make test     - Start Go test servers"
	@echo "  make stop     - Stop test servers"
	@echo "  make clean    - Cleanup project"
	@echo "  make setup    - Setup wordlists/results directories"

# -------------------------
# Python setup
# -------------------------
install: clean
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Installed. Use 'source $(VENV)/bin/activate' or 'make run'"

run: .check-venv
	$(PYTHON) main.py

# -------------------------
# Go test servers
# -------------------------
test: test-go

test-go:
	@bash -c '\
		pkill -f port_scanning_target 2>/dev/null || true; \
		pkill -f fuzz_target 2>/dev/null || true; \
		sleep 1; \
		\
		( cd tests/port_scanning && exec $(GO) run port_scanning_target.go > /dev/null 2>&1 ) & \
		echo $$! > $(PS_PID_FILE); \
		\
		( cd tests/fuzzing && exec $(GO) run fuzz_target.go > /dev/null 2>&1 ) & \
		echo $$! > $(FUZZ_PID_FILE); \
		\
		sleep 2; \
		echo "Servers started:"; \
		echo "  Port scanner PID: $$(cat $(PS_PID_FILE))"; \
		echo "  Fuzzer PID: $$(cat $(FUZZ_PID_FILE))"; \
	'

# -------------------------
# Stop servers
# -------------------------
stop:
	@bash -c '\
		pkill -f port_scanning_target 2>/dev/null || true; \
		pkill -f fuzz_target 2>/dev/null || true; \
		rm -f $(PS_PID_FILE) $(FUZZ_PID_FILE); \
		echo "Servers stopped"; \
	'

# -------------------------
# Project setup
# -------------------------
setup:
	mkdir -p wordlists results
	printf 'admin\nlogin\nrobots.txt\n.svn\n.git\nbackup\n' > wordlists/common.txt

# -------------------------
# Cleanup
# -------------------------
clean:
	rm -rf $(VENV) .pytest_cache results/ __pycache__/ **/__pycache__ .mypy_cache .ruff_cache
	rm -f $(PS_PID_FILE) $(FUZZ_PID_FILE)

# -------------------------
# Safety check
# -------------------------
.check-venv:
	@test -d $(VENV) || (echo "Run 'make install' first" && exit 1)
