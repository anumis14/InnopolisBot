n = int(input("Введите число: "))

def IsPrime(n):
    d = 2
    if n == 1:
        return True
    while n % d != 0:
        d += 1
    return d == n


if not IsPrime(n):
    print("Число не простое")
else:
    print("Число простое")