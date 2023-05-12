d=int(input())
n=int(input())
l=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
a=n*l
l=-3
for i in range(10000):
    l+=3
    if a<=d:
        print(l)
        break
    d=d+p1
    if a<=d:
        print(l+1)
        break
    d=d+p2
    if a<=d:
        print(l+2)
        break
    d=d+p3
    if a<=d:
        print(l+3)
        break