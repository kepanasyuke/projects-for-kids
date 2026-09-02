.PHONY: help rockets pizza train hero all check

help:
	@echo "Команды проекта:"
	@echo "  make rockets - запустить ракеты (list)"
	@echo "  make pizza   - приготовить пиццу (set)"
	@echo "  make train   - отправить поезд (linked list)"
	@echo "  make hero    - создать героя (dict)"
	@echo "  make all     - показать всё шоу"
	@echo "  make check   - проверить код без длинной анимации"

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
	@python3 -m py_compile main.py
	@python3 main.py --fast rockets >/dev/null
	@python3 main.py --fast pizza >/dev/null
	@python3 main.py --fast train >/dev/null
	@python3 main.py --fast hero >/dev/null
	@echo "Проверка пройдена!"
