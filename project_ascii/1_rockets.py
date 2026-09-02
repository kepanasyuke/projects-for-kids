"""Задание 1: список и ракеты."""

from common import clear_screen, pause, require_student_work, title


# ============================================================
# НАЧАЛО КОДА УЧЕНИКА
# Впиши 3 названия ракет в квадратных скобках и можешь добавить 4-е.
# Пример: ROCKET_COLORS = ["Молния", "Комета", "Звезда"]
ROCKET_COLORS = ["ВПИШИ_РАКЕТУ_1", "ВПИШИ_РАКЕТУ_2", "ВПИШИ_РАКЕТУ_3"]
# КОНЕЦ КОДА УЧЕНИКА
# ============================================================


def rockets_program() -> None:
    """Показывает, что list сохраняет порядок элементов."""
    if not require_student_work(
        ROCKET_COLORS,
        ["ВПИШИ_РАКЕТУ_1", "ВПИШИ_РАКЕТУ_2", "ВПИШИ_РАКЕТУ_3"],
        "1 — список",
        '["Молния", "Комета", "Звезда"]',
    ):
        return
    rocket = ["   /\\   ", "  |🚀|  ", " /|  |\\ ", "   /\\   "]
    title("🚀  РАКЕТНЫЙ СТАРТ: СПИСОК  🚀")
    print("\nСписок хранит элементы по порядку. Ракеты стартуют одна за другой!\n")
    pause(0.7)
    for color in ROCKET_COLORS:
        for position in range(0, 25, 3):
            clear_screen()
            title(f"🚀  РАКЕТА: {color}  🚀")
            print("\n" * 2)
            for line in rocket:
                print(" " * position + line)
            print("\n" + " " * position + "🔥🔥🔥")
            print(f"\nПолет ракеты «{color}»...")
            pause(0.06)
        print(f"✨ Ракета «{color}» улетела в космос! ✨")
        pause(0.4)
    print("\n✅ Все ракеты стартовали в порядке списка.")


if __name__ == "__main__":
    rockets_program()
