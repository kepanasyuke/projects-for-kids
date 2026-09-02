"""ASCII-модуль 2: четыре задания с множествами."""
import common

# НАЧАЛО КОДА УЧЕНИКА: впиши уникальные элементы в четыре множества.
INGREDIENTS = {"ВПИШИ_ПРОДУКТ_1", "ВПИШИ_ПРОДУКТ_2"}
STARS = {"ВПИШИ_ЗВЕЗДУ_1", "ВПИШИ_ЗВЕЗДУ_2"}
CRYSTALS = {"ВПИШИ_КРИСТАЛЛ_1", "ВПИШИ_КРИСТАЛЛ_2"}
SOUNDS = {"ВПИШИ_ЗВУК_1", "ВПИШИ_ЗВУК_2"}
# КОНЕЦ КОДА УЧЕНИКА


def play(title, data, picture):
    if any(str(item).startswith("ВПИШИ_") for item in data):
        common.title("GAME OVER: заполни задание")
        print(f"\n{title}: замени заглушки в module_2.py")
        return
    for step in range(8):
        common.clear_screen(); common.title(title)
        print(picture + "\n" + "  ".join(sorted(data))); common.pause(0.08)


def task_05(): play("05 · ПИЦЦА", INGREDIENTS, "      (  🍕  )")
def task_06(): play("06 · ЗВЁЗДНОЕ НЕБО", STARS, " *     ✦      *")
def task_07(): play("07 · КРИСТАЛЛЫ", CRYSTALS, "      /\\  /\\\n     <  ><  >")
def task_08(): play("08 · ЗВУКОВАЯ ВОЛНА", SOUNDS, " ~~~~ ~~~~ ~~~~")

PROGRAMS = [("Множество ингредиентов", task_05), ("Множество звёзд", task_06), ("Множество кристаллов", task_07), ("Множество звуков", task_08)]
