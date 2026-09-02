SHELL := /bin/bash
PORT ?= 8000

.PHONY: help run start kill-port status check

help:
	@echo "JS-проект: 28 заданий в 16 модулях"
	@echo "  make run       - освободить порт и запустить проект"
	@echo "  make start     - то же самое, что make run"
	@echo "  make kill-port - остановить сервер на порту $(PORT)"
	@echo "  make status    - проверить порт $(PORT)"
	@echo "  make check     - проверить синтаксис JavaScript"

run: kill-port
	@echo "Открой http://localhost:$(PORT)"
	@python3 -m http.server $(PORT)

start: run

kill-port:
	@pids=$$(lsof -ti :$(PORT) 2>/dev/null || true); \
	if [[ -n "$$pids" ]]; then \
		echo "Останавливаю процессы на порту $(PORT): $$pids"; \
		kill $$pids 2>/dev/null || true; \
	else \
		echo "Порт $(PORT) свободен"; \
	fi

status:
	@pids=$$(lsof -ti :$(PORT) 2>/dev/null || true); \
	if [[ -n "$$pids" ]]; then echo "Порт $(PORT) занят: $$pids"; else echo "Порт $(PORT) свободен"; fi

check:
	@for file in app.js extra_tasks.js module_*.js; do node --check "$$file" || exit 1; done
	@echo "JavaScript-проект проверен!"
