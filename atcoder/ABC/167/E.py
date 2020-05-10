def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p

N, M, K = map(int, input().split())

p = 998244353
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
col = M
for x in range(N - 1, -1, -1):
    now = col
    now *= cmb(N - 1, x, p)
    now %= p
    if x <= K:
        ans += now
        ans %= p
    col *= (M - 1)
    col %= p
print(ans)