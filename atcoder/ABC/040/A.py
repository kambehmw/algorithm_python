n, x = tuple(map(int, input().split()))
if n // 2 < x:
    print(n - x)
else:
    print(x - 1)