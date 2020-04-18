N = int(input())
digit = len(str(N))
ans = 0
for i in range(1, digit+1):
    a = N // (10 ** i) * 10 ** (i - 1)
    b = N % (10 ** i)
    if 2 * 10 ** (i - 1) <= b:
        b = 10 ** (i - 1)
    elif b < 10 ** (i - 1):
        b = 0
    else:
        b = b - 10 ** (i - 1) + 1
    ans += (a + b)
print(ans)
