"""ASCII-модуль 1: четыре задания со списками."""
import common

# НАЧАЛО КОДА УЧЕНИКА: заполни четыре списка.
ROCKETS = ["ВПИШИ_РАКЕТУ_1", "ВПИШИ_РАКЕТУ_2"]
PLANETS = ["ВПИШИ_ПЛАНЕТУ_1", "ВПИШИ_ПЛАНЕТУ_2"]
ROBOTS = ["ВПИШИ_РОБОТА_1", "ВПИШИ_РОБОТА_2"]
COLORS = ["ВПИШИ_ЦВЕТ_1", "ВПИШИ_ЦВЕТ_2"]
# КОНЕЦ КОДА УЧЕНИКА


def play(title, data, picture):
    if any(str(item).startswith("ВПИШИ_") for item in data):
        common.title("GAME OVER: заполни задание")
        print(f"\n{title}: замени заглушки в module_1.py")
        return
    for step in range(8):
        common.clear_screen(); common.title(title)
        print("\n" * (step % 3) + picture + "\n")
        print(" -> ".join(data)); common.pause(0.08)


def task_01(): play("01 · РАКЕТЫ", ROCKETS, "      /\\\n 🚀  |  |  🚀")
def task_02(): play("02 · ПЛАНЕТЫ", PLANETS, "       .-O-.\n   .-O-    -O-.")
def task_03(): play("03 · РОБОТЫ", ROBOTS, "   [o_o]  [o_o]\n     /|    /|")
def task_04(): play("04 · ЦВЕТНАЯ БАШНЯ", COLORS, "       []\n      [][]\n     [][][]")

PROGRAMS = [("Список ракет", task_01), ("Список планет", task_02), ("Очередь роботов", task_03), ("Башня цветов", task_04)]
