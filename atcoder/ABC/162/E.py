N, K = map(int, input().split())
mod = 10 ** 9 + 7
d = [0] * (K + 1)
for i in range(1, K + 1):
    d[i] = pow(K // i, N, mod)
for i in range(K, 0, -1):
    for j in range(2 * i , K + 1, i):
        d[i] -= d[j]
        d[i] %= mod
ans = 0
for i in range(1, K + 1):
    ans += d[i] * i
    ans %= mod
print(ans)