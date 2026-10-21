MAX_SCORE = 5
ALFEROV_YEAR = 1930
MAX_ATTEMPTS = 5

QUESTIONS = [
    {
        "text": "Что такое фишинг?",
        "options": {
            "A": "Мошенничество с целью получить пароли и данные через поддельные письма/сайты",
            "B": "Программа для защиты компьютера от вирусов",
        },
        "correct": "A",
    },
    {
        "text": "Какой пароль надёжнее?",
        "options": {
            "A": "123456 или qwerty",
            "B": "Длинная фраза с буквами, цифрами и символами",
        },
        "correct": "B",
    },
    {
        "text": "Для чего нужна двухфакторная аутентификация (2FA)?",
        "options": {
            "A": "Чтобы ускорить вход в аккаунт без пароля",
            "B": "Чтобы подтвердить вход вторым способом (код, приложение, SMS)",
        },
        "correct": "B",
    },
    {
        "text": "Что следует делать с подозрительным вложением в письме?",
        "options": {
            "A": "Открыть и проверить, что внутри",
            "B": "Не открывать и сообщить администратору / удалить письмо",
        },
        "correct": "B",
    },
]


def ask_choice(num, q):
    print(f"\nВопрос {num}. {q['text']}")
    for key, val in q["options"].items():
        print(f"  {key}) {val}")

    while True:
        ans = input("Ваш ответ (A/B): ").strip().upper()
        if ans in q["options"]:
            break
        print("Введите A или B.")

    if ans == q["correct"]:
        print("Верно!")
        return 1
    print("Неверно.")
    return 0


def ask_alferov_year():
    left = MAX_ATTEMPTS
    print("\nВопрос 5. В каком году родился лауреат Нобелевской премии")
    print("          Жорес Иванович Алфёров?")
    print("Подсказка: примерный диапазон — между 1925 и 1935 годом.")

    while left > 0:
        raw = input("Введите год рождения: ").strip()
        if raw.isdigit() and int(raw) == ALFEROV_YEAR:
            print("Верно!")
            return 1
        left -= 1
        print(f"Не верно, попробуйте снова. Осталось попыток: {left}")

    print(f"Попытки закончились. Правильный ответ: {ALFEROV_YEAR} год.")
    return 0


def get_grade(score):
    return {5: 5, 4: 4, 3: 3, 2: 2}.get(score, 2)


def main():
    print("=" * 50)
    print("  ТЕСТ: Информационная безопасность")
    print("=" * 50)
    print("Ответьте на 5 вопросов. За каждый верный ответ — 1 балл.")

    score = sum(ask_choice(i + 1, q) for i, q in enumerate(QUESTIONS))
    score += ask_alferov_year()

    print("\n" + "=" * 50)
    print("  РЕЗУЛЬТАТ")
    print("=" * 50)
    print(f"Набрано баллов: {score} из {MAX_SCORE}")
    print(f"Оценка: {get_grade(score)}")
    print("=" * 50)


if __name__ == "__main__":
    main()
