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
	@python3 -m py_compile main.py common.py 1_rockets.py 2_pizza.py 3_train.py 4_hero.py
	@python3 main.py --fast rockets >/dev/null
	@python3 main.py --fast pizza >/dev/null
	@python3 main.py --fast train >/dev/null
	@python3 main.py --fast hero >/dev/null
	@echo "ASCII-проект проверен!"
