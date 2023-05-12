a = int(input())
b = int(input())
t = int(input())

if a == t or b == t or t % a == 0 or t % b == 0:
    print("0")
else:
    a1 = a-(t - a*(t//a))
    b1 = b-(t - b*(t//b))
    print(min(a1,b1))