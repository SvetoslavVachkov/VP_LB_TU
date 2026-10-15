def exercise_1():
    print("\n--- Задача 1: Най-голямо число ---")
    n = int(input("Въведете брой числа (n > 0): "))
    if n <= 0:
        print("Невалиден брой!")
        return
    max_num = int(input("Въведете число: "))
    for _ in range(n - 1):
        num = int(input("Въведете число: "))
        if num > max_num:
            max_num = num
    print(f"Най-голямото число е: {max_num}")

def exercise_2():
    print("\n--- Задача 2: Сумиране на n числа ---")
    n = int(input("Въведете брой числа: "))
    total_sum = 0
    for _ in range(n):
        num = int(input("Въведете число: "))
        total_sum += num
    print(f"Сумата на числата е: {total_sum}")

def exercise_3():
    print("\n--- Задача 3: Триъгълник от звездички ---")
    n = int(input("Въведете число n: "))
    for i in range(1, n + 1):
        print('*' * i)

def exercise_4():
    print("\n--- Задача 4: Проверка за просто число ---")
    n = int(input("Въведете число: "))
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
    if prime:
        print(f"Числото {n} е просто.")
    else:
        print(f"Числото {n} е съставно.")

def exercise_5():
    print("\n--- Задача 5: Ден от седмицата ---")
    day = int(input("Въведете номер на ден (1-7): "))
    if day == 1:
        print(f"{day} - Понеделник")
    elif day == 2:
        print(f"{day} - Вторник")
    elif day == 3:
        print(f"{day} - Сряда")
    elif day == 4:
        print(f"{day} - Четвъртък")
    elif day == 5:
        print(f"{day} - Петък")
    elif day == 6:
        print(f"{day} - Събота")
    elif day == 7:
        print(f"{day} - Неделя")
    else:
        print(f"{day} - Невалиден номер на ден!")

def exercise_6():
    print("\n--- Задача 6: Проверка на интервал [1; 10] ---")
    n = float(input("Въведете число: "))
    if 1 <= n <= 10:
        print(f"Числото {n} е в интервала [1; 10].")
    else:
        print(f"Числото {n} е ИЗВЪН интервала [1; 10].")

def exercise_7():
    print("\n--- Задача 7: Прост калкулатор ---")
    a = float(input())
    op = input()
    b = float(input())
    
    if op == '+':
        print(f"Резултат: {a + b}")
    elif op == '-':
        print(f"Резултат: {a - b}")
    elif op == '*':
        print(f"Резултат: {a * b}")
    elif op == '/':
        if b == 0:
            print("Грешка: Деление на нула!")
        else:
            print(f"Резултат: {a / b}")
    else:
        print("Невалидна операция!")

def exercise_8():
    print("\n--- Задача 8: Брой числа в зададени граници ---")
    min_val = float(input("Въведете долна граница: "))
    max_val = float(input("Въведете горна граница: "))
    count = 0
    print("Въведете поредица от 10 числа:")
    for i in range(1, 11):
        num = float(input(f"Число {i}: "))
        if min_val <= num <= max_val:
            count += 1
    print(f"Брой числа в интервала [{min_val}; {max_val}]: {count}")

def main():
    exercises = [None, exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6, exercise_7, exercise_8]
    choice = int(input("Задача:"))
    if 1 <= choice <= 8:
        exercises[choice]()
    elif choice == 0:
        pass
    else:
        print("Невалиден избор.")

if __name__ == "__main__":
    main()