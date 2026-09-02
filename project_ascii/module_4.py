"""ASCII-модуль 4: четыре задания со словарями."""
import common

# НАЧАЛО КОДА УЧЕНИКА: заполни характеристики четырёх персонажей.
HERO = {"имя": "ВПИШИ_ИМЯ", "сила": "ВПИШИ_СИЛУ"}
PET = {"имя": "ВПИШИ_ИМЯ_ПИТОМЦА", "талант": "ВПИШИ_ТАЛАНТ"}
WIZARD = {"имя": "ВПИШИ_ИМЯ_МАГА", "заклинание": "ВПИШИ_ЗАКЛИНАНИЕ"}
ASTRONAUT = {"имя": "ВПИШИ_ИМЯ_КОСМОНАВТА", "планета": "ВПИШИ_ПЛАНЕТУ"}
# КОНЕЦ КОДА УЧЕНИКА


def play(title, data):
    if any(str(value).startswith("ВПИШИ_") for value in data.values()):
        common.title("GAME OVER: заполни задание")
        print(f"\n{title}: замени заглушки в module_4.py")
        return
    for key, value in data.items():
        common.clear_screen(); common.title(title)
        print("\n        O\n       /|\\\n       / \\")
        print(f"\n{key}: {value}"); common.pause(0.5)


def task_13(): play("13 · ГЕРОЙ", HERO)
def task_14(): play("14 · ПИТОМЕЦ", PET)
def task_15(): play("15 · ВОЛШЕБНИК", WIZARD)
def task_16(): play("16 · КОСМОНАВТ", ASTRONAUT)

PROGRAMS = [("Словарь героя", task_13), ("Словарь питомца", task_14), ("Словарь волшебника", task_15), ("Словарь космонавта", task_16)]
