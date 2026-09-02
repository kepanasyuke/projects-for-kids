"""Задание 3: связный список и ASCII-поезд."""

from dataclasses import dataclass

import common


# ============================================================
# НАЧАЛО КОДА УЧЕНИКА
# Впиши названия вагонов и вставь новый вагон через insert.
# Пример: TRAIN_CARS.insert(2, "Вагон-лаборатория")
TRAIN_CARS = ["ВПИШИ_ПАРОВОЗ", "ВПИШИ_ВАГОН_1", "ВПИШИ_ВАГОН_2", "ВПИШИ_ВАГОН_3"]
TRAIN_CARS.insert(2, "ВПИШИ_НОВЫЙ_ВАГОН")
# КОНЕЦ КОДА УЧЕНИКА
# ============================================================

TEMPLATE = ["ВПИШИ_ПАРОВОЗ", "ВПИШИ_ВАГОН_1", "ВПИШИ_НОВЫЙ_ВАГОН", "ВПИШИ_ВАГОН_2", "ВПИШИ_ВАГОН_3"]


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


def train_program() -> None:
    if TRAIN_CARS == TEMPLATE or any(name.startswith("ВПИШИ_") for name in TRAIN_CARS):
        common.clear_screen()
        common.title("GAME OVER: СНАЧАЛА СОБЕРИ ПОЕЗД")
        print('\nЗамени заглушки в блоке КОДА УЧЕНИКА файла 3_train.py.')
        print('Пример: TRAIN_CARS.insert(2, "Вагон-лаборатория")')
        return
    train = build_train(TRAIN_CARS)
    names = []
    while train:
        names.append(train.name)
        train = train.next
    for position in range(0, 30, 3):
        common.clear_screen()
        common.title("ASCII-ПОЕЗД · СВЯЗНЫЙ СПИСОК")
        print(" " * position + "🚂 " + "—".join(f"[{name}]" for name in names))
        print(" " * position + "════════════════════════════════════")
        common.pause(0.08)
    print("\n✅ Каждый вагон связан с следующим через поле next.")


if __name__ == "__main__":
    train_program()
