"""ASCII-модуль 3: четыре задания с цепочками."""
import common

# НАЧАЛО КОДА УЧЕНИКА: составь четыре цепочки.
TRAIN = ["ВПИШИ_ПАРОВОЗ", "ВПИШИ_ВАГОН"]
FRIENDS = ["ВПИШИ_ДРУГА_1", "ВПИШИ_ДРУГА_2"]
STATIONS = ["ВПИШИ_СТАНЦИЮ_1", "ВПИШИ_СТАНЦИЮ_2"]
NOTES = ["ВПИШИ_НОТУ_1", "ВПИШИ_НОТУ_2"]
# КОНЕЦ КОДА УЧЕНИКА


def play(title, data, picture):
    if any(str(item).startswith("ВПИШИ_") for item in data):
        common.title("GAME OVER: заполни задание")
        print(f"\n{title}: замени заглушки в module_3.py")
        return
    for step in range(8):
        common.clear_screen(); common.title(title)
        print("\n" + picture + "\n" + " -> ".join(data)); common.pause(0.08)


def task_09(): play("09 · ПОЕЗД", TRAIN, "🚂 [вагон] [вагон]")
def task_10(): play("10 · ДРУЗЬЯ", FRIENDS, "🙂 — 🙂 — 🙂")
def task_11(): play("11 · МАРШРУТ", STATIONS, "●━━━━●━━━━●")
def task_12(): play("12 · МЕЛОДИЯ", NOTES, "♪  ♫  ♪  ♫")

PROGRAMS = [("Связный поезд", task_09), ("Цепочка друзей", task_10), ("Маршрут станций", task_11), ("Цепочка нот", task_12)]
