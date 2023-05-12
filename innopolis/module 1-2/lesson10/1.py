# Написать простой калькулятор с использованием функций.
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))


def calc(a, b):
    choice = int(input("Какую операцию вы хотите сделать?\n1-Сумма\n2-Вычитание\n3-Умножение\n4-Деление\nОтвет: "))

    if choice == 1:
        def summa(a,b):
            print(a+b)
        summa(a, b)
    elif choice == 2:
        def minus(a, b):
            print(a-b)
        minus(a, b)
    elif choice == 3:
        def get_multi(a, b):
            print(a*b)
        get_multi(a, b)
    elif choice == 4:
        def get_division(a, b):
            if b == 0:
                print("На ноль делить нельзя!")
            else:
                print(a//b)
        get_division(a, b)


calc(a, b)
