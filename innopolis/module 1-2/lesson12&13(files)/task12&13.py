# Написать программу список дел, которая спрашивает у пользователя значение n
# после этого запрашивает на ввод n строк различных дел и сохраняет их в список
# а после записывает значения из списка через одно в файл в одну строку.



n = int(input("Введите количество дел: "))
l = []
for i in range(n):
    task = str(input("Введите дело: "))
    l.append(task)


with open('business.txt', "w+", encoding="utf-8") as file:
    for element in l:
        file.writelines(element + "\n")
