n, m, d = map(int, input().split())
if d == 0:
    print(n / (n ** 2) * (m - 1))
else:
    print(2 * (n - d) / (n ** 2) * (m - 1))