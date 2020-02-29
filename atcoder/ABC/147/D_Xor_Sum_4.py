N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7


def mod_pow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        half_p = p // 2
        half = mod_pow(a, half_p)
        return half * half % mod
    else:
        return a * mod_pow(a, p - 1) % mod


ans = 0
for i in range(60):
    cnt = 0
    for a in A:
        if a >> i & 1:
            cnt += 1
    now = cnt * (N - cnt) % mod
    ans += now * mod_pow(2, i) % mod
    ans %= mod
print(ans)
