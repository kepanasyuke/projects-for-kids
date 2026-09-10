# Makefile для "Мастерская Шестерёнкина"
# Игра — один index.html без сборки, нужен только локальный HTTP-сервер.

PORT ?= 8000
URL  := http://localhost:$(PORT)

.PHONY: help setup run dev port kill-port stop clean all

help:
	@echo "══════ Мастерская Шестерёнкина ══════"
	@echo "  make setup     — проверить окружение (python3/node)"
	@echo "  make run       — запустить сервер на порту $(PORT)"
	@echo "  make dev       — алиас для run"
	@echo "  make port      — показать порт и URL"
	@echo "  make kill-port — остановить процесс на порту $(PORT)"
	@echo "  make stop      — то же, что kill-port"
	@echo "  make clean     — удалить temp (node_modules, .cache)"
	@echo "  make all       — setup + run"

# ---------- ОКРУЖЕНИЕ ----------
setup:
	@echo "→ Проверяю окружение..."
	@(python3 --version >/dev/null 2>&1 && echo "✓ python3: $$(python3 --version 2>&1)") || \
	 (echo "✓ python3: не найден")
	@(node --version >/dev/null 2>&1 && echo "✓ node: $$(node --version 2>&1)") || \
	 (echo "✓ node: не найден (можно через python3)")
	@echo "Готово. Запустите: make run"

# ---------- СЕРВЕР ----------
run: setup
	@echo "→ Запускаю сервер на $(URL)"
	@if python3 --version >/dev/null 2>&1; then \
		echo "Использую python3 (http.server)"; \
		python3 -m http.server $(PORT); \
	elif node --version >/dev/null 2>&1 && command -v npx >/dev/null 2>&1; then \
		echo "Использую npx http-server"; \
		npx --yes http-server . -p $(PORT) -c-1; \
	else \
		echo "ОШИБКА: нужен python3 или node+npx для запуска."; exit 1; \
	fi

dev: run

# ---------- ПОРТ ----------
port:
	@echo "Порт: $(PORT)"
	@echo "URL : $(URL)"

# ---------- ОСТАНОВКА ----------
kill-port:
	@echo "→ Ищу процессы на порту $(PORT)..."
	@if command -v lsof >/dev/null 2>&1; then \
		PIDS=$$(lsof -ti:$(PORT) 2>/dev/null); \
		if [ -n "$$PIDS" ]; then \
			echo "Останавливаю: $$PIDS"; kill $$PIDS; \
			echo "✓ Порт $(PORT) освобождён"; \
		else \
			echo "На порту $(PORT) никого нет."; \
		fi; \
	elif command -v fuser >/dev/null 2>&1; then \
		PIDS=$$(fuser $(PORT)/tcp 2>/dev/null); \
		if [ -n "$$PIDS" ]; then \
			echo "Останавливаю: $$PIDS"; kill $$PIDS; \
			echo "✓ Порт $(PORT) освобождён"; \
		else \
			echo "На порту $(PORT) никого нет."; \
		fi; \
	else \
		echo "Нет lsof/fuser. Найди процесс вручную:"; \
		echo "  ps aux | grep 8000"; \
	fi

stop: kill-port

# ---------- ОЧИСТКА ----------
clean:
	@echo "→ Удаляю временные файлы..."
	@rm -rf node_modules .cache .coverage 2>/dev/null; true
	@echo "✓ Чисто"

# ---------- ВСЁ СРАЗУ ----------
all: setup run