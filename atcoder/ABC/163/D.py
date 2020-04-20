N, K = map(int, input().split())
mod = 10 ** 9 + 7
x = [i for i in range(N+1)]
y = [0] * (N + 2)
z = [0] * (N + 2)
for i in range(N+1):
    y[i + 1] = y[i] + x[i]
    z[i + 1] = z[i] + x[N-i]
# print(y)
# print(z)
ans = 0
for i in range(K, N+2):
    ans += z[i] - y[i] + 1
    ans %= mod
print(ans)