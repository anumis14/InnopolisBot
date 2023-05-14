a= int(input("Введи число: "))
if a%10==1 and a%100!=11:
    print(a,"компьютер")
elif a%100 == 12 or a%100 == 13 or a%100 == 14:
    print(a,"компьютеров")
elif (a%10==2 or a%10==3 or a%10==4):
    print(a,"компьютера")
else:
    print(a,"компьютеров")