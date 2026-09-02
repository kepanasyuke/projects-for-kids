#!/usr/bin/env python3
"""Меню 16 ASCII-заданий, разделённых на четыре модуля."""

import argparse

import common
from module_1 import PROGRAMS as MODULE_1
from module_2 import PROGRAMS as MODULE_2
from module_3 import PROGRAMS as MODULE_3
from module_4 import PROGRAMS as MODULE_4
from module_5 import PROGRAMS as MODULE_5
from module_6 import PROGRAMS as MODULE_6
from module_7 import PROGRAMS as MODULE_7
from module_8 import PROGRAMS as MODULE_8
from module_9 import PROGRAMS as MODULE_9
from module_10 import PROGRAMS as MODULE_10
from module_11 import PROGRAMS as MODULE_11
from module_12 import PROGRAMS as MODULE_12
from module_13 import PROGRAMS as MODULE_13
from module_14 import PROGRAMS as MODULE_14
from module_15 import PROGRAMS as MODULE_15
from module_16 import PROGRAMS as MODULE_16

PROGRAMS = MODULE_1 + MODULE_2 + MODULE_3 + MODULE_4 + MODULE_5 + MODULE_6 + MODULE_7 + MODULE_8 + MODULE_9 + MODULE_10 + MODULE_11 + MODULE_12 + MODULE_13 + MODULE_14 + MODULE_15 + MODULE_16


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true")
    args = parser.parse_args()
    common.set_fast(args.fast)

    while True:
        common.clear_screen()
        common.title("ASCII · 16 ЗАДАНИЙ · 4 МОДУЛЯ")
        for number, (name, _) in enumerate(PROGRAMS, 1):
            print(f"{number:02}. {name}")
        print("00. Выйти")
        choice = input("\nВыбери номер: ").strip()
        if choice == "00":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(PROGRAMS):
            PROGRAMS[int(choice) - 1][1]()
            input("\nEnter — назад в меню...")


if __name__ == "__main__":
    main()
