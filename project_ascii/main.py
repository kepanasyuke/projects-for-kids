#!/usr/bin/env python3
"""Главное меню проекта."""

import argparse
import importlib

import common

rockets_program = importlib.import_module("1_rockets").rockets_program
pizza_program = importlib.import_module("2_pizza").pizza_program
train_program = importlib.import_module("3_train").train_program
hero_program = importlib.import_module("4_hero").hero_program


# Каждая функция в этом словаре запускает отдельное задание.
PROGRAMS = {
    "rockets": ("Ракеты — список", rockets_program),
    "pizza": ("Пицца — множество", pizza_program),
    "train": ("Поезд — связный список", train_program),
    "hero": ("Герой — словарь", hero_program),
}


def all_programs() -> None:
    """Запускает четыре учебные подпрограммы по очереди."""
    common.clear_screen()
    common.title("🎇  СУПЕР-ШОУ СТРУКТУР ДАННЫХ  🎇")
    print("\nСегодня оживут список, множество, связный список и словарь!\n")
    common.pause(1)
    for name, program in PROGRAMS.values():
        common.clear_screen()
        common.title(f"Следующая часть: {name}")
        common.pause(0.5)
        program()
        common.pause(1)
    print("\n🎉 Шоу завершено! Ты познакомился с четырьмя структурами данных.")


def show_menu() -> None:
    """Показывает меню и запускает выбранную подпрограмму."""
    while True:
        common.clear_screen()
        common.title("🎮  ШОУ СТРУКТУР ДАННЫХ  🎮")
        print("\n1. 🚀 Ракеты — список")
        print("2. 🍕 Пицца — множество")
        print("3. 🚂 Поезд — связный список")
        print("4. 🧙 Герой — словарь")
        print("5. 🎇 Запустить всё")
        print("0. Выйти")
        choice = input("\nВыбери номер: ").strip()
        if choice == "0":
            print("До встречи!")
            return
        if choice == "5":
            all_programs()
            input("\nНажми Enter, чтобы вернуться в меню...")
            continue
        scene_names = {"1": "rockets", "2": "pizza", "3": "train", "4": "hero"}
        scene = scene_names.get(choice)
        if scene:
            PROGRAMS[scene][1]()
            input("\nНажми Enter, чтобы вернуться в меню...")


def main() -> None:
    parser = argparse.ArgumentParser(description="Шоу структур данных для начинающих")
    parser.add_argument("--fast", action="store_true", help="быстрый режим для проверки")
    parser.add_argument("scene", nargs="?", choices=[*PROGRAMS, "all"])
    args = parser.parse_args()
    common.set_fast(args.fast)

    if args.scene == "all":
        all_programs()
    elif args.scene:
        PROGRAMS[args.scene][1]()
    else:
        show_menu()


if __name__ == "__main__":
    main()
