.PHONY: help rockets pizza train hero all check

help:
	@echo "ASCII-проект: четыре подпрограммы"
	@echo "  make rockets - ракеты (список)"
	@echo "  make pizza   - пицца (множество)"
	@echo "  make train   - поезд (связный список)"
	@echo "  make hero    - герой (словарь)"
	@echo "  make all     - все сцены"
	@echo "  make check   - проверка кода"

rockets:
	@python3 main.py rockets
pizza:
	@python3 main.py pizza
train:
	@python3 main.py train
hero:
	@python3 main.py hero
all:
	@python3 main.py all

check:
	@python3 -m py_compile main.py common.py module_*.py
	@echo "ASCII-проект проверен!"
