result = 1
a = [1, 2, 3, 4]

for i in range(0, len(a)):
    result = result * a[i]

print(f"Список {a}")
print(f'Произведение списка: {result}')
print(f'Сумма списка: {sum(a)}')