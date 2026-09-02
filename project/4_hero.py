"""Задание 4: словарь и герой."""

from common import clear_screen, pause, require_student_work, title


# ============================================================
# НАЧАЛО КОДА УЧЕНИКА
# Измени все 4 значения справа или добавь новую пару "ключ": "значение".
# Пример: "костюм": "Плащ-невидимка"
HERO = {
    "волосы": "ВПИШИ_ПРИЧЕСКУ",
    "глаза": "ВПИШИ_ГЛАЗА",
    "сила": "ВПИШИ_СУПЕРСИЛУ",
    "оружие": "ВПИШИ_ОРУЖИЕ",
}
# КОНЕЦ КОДА УЧЕНИКА
# ============================================================


def hero_program() -> None:
    template = {
        "волосы": "ВПИШИ_ПРИЧЕСКУ",
        "глаза": "ВПИШИ_ГЛАЗА",
        "сила": "ВПИШИ_СУПЕРСИЛУ",
        "оружие": "ВПИШИ_ОРУЖИЕ",
    }
    if not require_student_work(
        HERO,
        template,
        "4 — словарь",
        '"сила": "Полёт", "оружие": "Меч-молния"',
    ):
        return
    portal = ["      .      ", "    .:::.'    ", "  .:::::::::.  ", "    ':::::'    ", "      '      "]
    title("🧙  ПОРТАЛ ГЕРОЕВ: СЛОВАРЬ  🧙")
    print("\nПортал открывается...\n")
    for _ in range(2):
        for frame in portal:
            clear_screen()
            title("🌀  ПОРТАЛ АКТИВИРУЕТСЯ  🌀")
            print(frame.center(60))
            pause(0.08)
    hero = ["       O       ", "      /|\\      ", "      / \\      "]
    for key, value in HERO.items():
        clear_screen()
        title("🧙  ГЕРОЙ МАТЕРИАЛИЗУЕТСЯ  🧙")
        print("\n".join(hero).center(60))
        print(f"\n✨ {key}: {value} ✨".center(60))
        pause(0.55)
    clear_screen()
    title("🧙  ГЕРОЙ ГОТОВ!  🧙")
    print("\n".join(hero).center(60))
    print()
    for key, value in HERO.items():
        print(f"  {key.capitalize():12} : {value}")
    print("\n✅ Словарь находит значение по ключу.")


if __name__ == "__main__":
    hero_program()
