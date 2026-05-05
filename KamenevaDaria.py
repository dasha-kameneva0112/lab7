import random

total_attempts = 0  # commit 1

def generate_example():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
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

def math_quiz():
    score = 0
    total = 5
    
    print("МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР")
    print(f"Реши {total} примеров")
    
    for i in range(total):
        example, correct = generate_example()
        print(f"\nПример №{i+1}: {example} = ?")

        global total_attempts
        total_attempts += 1  # commit 2

        try:
            answer = int(input("Твой ответ: "))
            if answer == correct:
                print("Правильно!")
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
            print("Неплохо, но можно лучше")
        else:
            print("Нужно подтянуть математику")

def show_stats():
    global total_attempts
    print(f"\nПопыток за всё время: {total_attempts}")  # commit 3

while True:
    print("\n1. Начать тренировку")
    print("0. Выйти")
    
    choice = input("Выбери: ")
    if choice == "0":
        print("Успехов в учебе!")
        break
    elif choice == "1":
        math_quiz()
    else:
        print("Некорректный ввод!")