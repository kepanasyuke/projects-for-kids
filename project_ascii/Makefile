.PHONY: help run check

help:
	@echo "ASCII-проект: 28 заданий в 16 модулях"
	@echo "  make run   - открыть меню всех заданий"
	@echo "  make check - проверить модули"

run:
	@python3 main.py

check:
	@python3 -m py_compile main.py common.py module_*.py
	@echo "ASCII-проект проверен!"
