"""Задание 3: связный список и поезд."""

from dataclasses import dataclass

from common import clear_screen, pause, require_student_work, title


# ============================================================
# НАЧАЛО КОДА УЧЕНИКА
# Напиши 4 вагона и вставь свой вагон в середину состава.
# Пример: TRAIN_CARS.insert(2, "Вагон-лаборатория")
TRAIN_CARS = ["ВПИШИ_ПАРОВОЗ", "ВПИШИ_ВАГОН_1", "ВПИШИ_ВАГОН_2", "ВПИШИ_ВАГОН_3"]
TRAIN_CARS.insert(2, "ВПИШИ_НОВЫЙ_ВАГОН")
# КОНЕЦ КОДА УЧЕНИКА
# ============================================================


@dataclass
class Car:
    name: str
    next: "Car | None" = None


def build_train(names: list[str]) -> Car:
    first = Car(names[0])
    current = first
    for name in names[1:]:
        current.next = Car(name)
        current = current.next
    return first


def train_names(first_car: Car | None) -> list[str]:
    names: list[str] = []
    current = first_car
    while current is not None:
        names.append(current.name)
        current = current.next
    return names


def train_program() -> None:
    template = ["ВПИШИ_ПАРОВОЗ", "ВПИШИ_ВАГОН_1", "ВПИШИ_НОВЫЙ_ВАГОН", "ВПИШИ_ВАГОН_2", "ВПИШИ_ВАГОН_3"]
    if not require_student_work(
        TRAIN_CARS,
        template,
        "3 — связный список",
        'TRAIN_CARS.insert(2, "Вагон-лаборатория")',
    ):
        return
    title("🚂  ПОЕЗД: СВЯЗНЫЙ СПИСОК  🚂")
    print("\nВ каждом вагоне есть ссылка на следующий вагон. Поезд отправляется!\n")
    pause(0.7)
    cars = train_names(build_train(TRAIN_CARS))
    for position in range(0, 31, 3):
        clear_screen()
        title("🚂  ПОЕЗД ДВИЖЕТСЯ  🚂")
        print("\n" * 2)
        print(" " * position + "🚂  " + "—".join(f"[{car}]" for car in cars[:4]))
        print(" " * position + "══════════════════════════════════════════")
        print(f"\nВ составе вагонов: {len(cars)}")
        pause(0.1)
    clear_screen()
    title("🚉  ПОЕЗД ПРИБЫЛ  🚉")
    print("\nЦепочка вагонов:\n")
    for number, car in enumerate(cars, start=1):
        arrow = "  ↓" if number < len(cars) else "  (конец)"
        print(f"  {number}. {car}{arrow}")
        pause(0.18)


if __name__ == "__main__":
    train_program()
