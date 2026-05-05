import random

total_attempts = 0  # commit 1
difficulty = "medium"  # commit 6: easy/medium/hard

def generate_example():
    global difficulty
    if difficulty == "easy":
        max_num = 10
    elif difficulty == "hard":
        max_num = 50
    else:
        max_num = 20
    a = random.randint(1, max_num)  # commit 6
    b = random.randint(1, max_num)  # commit 6
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        result = a + b
        example = f"{a} + {b}"
    else:
        if op == '-':
            a, b = max(a, b), min(a, b)
            result = a - b
            example = f"{a} - {b}"
        else:
            result = a * b
            example = f"{a} × {b}"
    return example, result

def set_difficulty():
    global difficulty
    print("\n1. Лёгкая (1-10)")
    print("2. Средняя (1-20)")
    print("3. Сложная (1-50)")
    choice = input("Выбери: ")
    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("Оставлена текущая")  # commit 7

def math_quiz():
    score = 0
    total = 5
    
    print("МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР (лучший🤩)")  # commit 5
    print(f"Реши {total} примеров")
    
    for i in range(total):
        example, correct = generate_example()
        print(f"\nПример №{i+1}: {example} = ?")

        global total_attempts
        total_attempts += 1  # commit 2

        try:
            answer = int(input("Твой ответ: "))
            if answer == correct:
                print("Правильно! +1 балл✅")  # commit 9
                score += 1
            else:
                print(f"Неверно! Правильный ответ: {correct}")
        except ValueError:
            print("Ошибка! Принимаются только числа")
            break
    
    print(f"Итог: {score}/{total}")
    if score == total:
        print("Отлично! Ты гений!")
    else: 
        if score >= total/2:
            print("Неплохо, но можно лучше (попробуй сложность легче)")  # commit 10
        else:
            print("Нужно подтянуть математику")

def show_stats():
    global total_attempts
    print("СТАТИСТИКА")  # commit 11
    print(f"\nПопыток за всё время: {total_attempts}")  # commit 3

while True:
    print("\n1. Начать тренировку")
    print("2. Показать статистику")  # commit 4
    print("3. Выбрать сложность")  # commit 8
    print("0. Выйти")
    
    choice = input("Выбери: ")
    if choice == "0":
        print("Успехов в учебе!")
        break
    elif choice == "1":
        math_quiz()
    elif choice == "2":
        show_stats()  # commit 4
    elif choice == "3":
        set_difficulty()  # commit 8
    else:
        print("Некорректный ввод!")