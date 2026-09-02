"""Общие функции для всех сцен."""

import os
import time

FAST = False


def set_fast(value: bool) -> None:
    global FAST
    FAST = value


def pause(seconds: float) -> None:
    if not FAST:
        time.sleep(seconds)


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def title(text: str) -> None:
    print("=" * 60)
    print(text.center(60))
    print("=" * 60)


def require_student_work(current, template, task: str, example: str) -> bool:
    """Не запускает сцену, пока ученик не заменит заглушки."""
    if current != template:
        return True
    clear_screen()
    title(f"📝  СНАЧАЛА ВЫПОЛНИ ЗАДАНИЕ: {task}  📝")
    print("\nТы пока оставил пример-заглушку без изменений.")
    print("Замени данные между комментариями КОДА УЧЕНИКА.")
    print(f"\nПример: {example}")
    print("\nПосле этого запусти сцену ещё раз.")
    return False
