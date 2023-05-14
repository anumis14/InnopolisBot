sum = 0
n = 1000
l = list(range(1, n))
for i in l:
    if i % 5 == 0 or i % 3 == 0:
        sum += i
print(sum)