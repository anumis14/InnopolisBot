n = int(input())
k = int(input())

a = []
ans = 0

if n % (k + 1) == 0:
    ans = n // (k + 1)
    print(ans)
else:
    print((n - (k+1))%k)
