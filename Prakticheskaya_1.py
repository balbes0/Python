import math

def numx(sms):
    while True:
        try:
            num = float(input(sms))
            return num
        except ValueError:
            print("Введите корректное число.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    print("Выберите номер операции который вы хотите выполнить:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - Возведение в степень")
    print("6 - Квадратный корень")
    print("7 - Факториал")
    print("8 - Синус")
    print("9 - Косинус")
    print("10 - Тангенс")
    print("0 - Выход")

    oper = int(input("Введите номер операции: "))

    if oper == '0':
        print("До свидания!")
        break
    elif oper == 1 or oper == 2 or oper == 3 or oper == 4 or oper == 5:
        num1 = numx("Введите первое число: ")
        num2 = numx("Введите второе число: ")

        if oper == 1:
            otvet = num1 + num2
        elif oper == 2:
            otvet = num1 - num2
        elif oper == 3:
            otvet = num1 * num2
        elif oper == 4:
            if num2 == 0:
                print("Ошибка: деление на ноль.")
                continue
            otvet = num1 / num2
        elif oper == '5':
            otvet = num1 ** num2

        print("Результат:", otvet)
    elif oper == 6:
        num = numx("Введите число для извлечения квадратного корня: ")
        if num < 0:
            print("Нельзя извлекать корень из отрицательного числа.")
            continue
        otvet = math.sqrt(num)
        print("Результат:", otvet)
    elif oper == 7:
        num = int(numx("Введите число для вычисления факториала: "))
        if num < 0:
            print("Нельзя вычислить факториал отрицательного числа.")
            continue
        otvet = factorial(num)
        print("Результат: ", otvet)
    elif oper == 8 or oper == 9 or oper == 10:
        num = numx("Введите угол в радианах: ")
        if oper == 8:
            otvet = math.sin(num)
        elif oper == 9:
            otvet = math.cos(num)
        elif oper == 10:
            otvet = math.tan(num)
        print("Результат: ", otvet)
    else:
        print("Некорректный выбор операции")