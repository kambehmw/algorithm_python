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


def calc_comb(a, b):
    if b > a - b:
        return calc_comb(a, a - b)

    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= (a - i)
        ans_div *= (i + 1)
        ans_mul %= mod
        ans_div %= mod

    ans = ans_mul * mod_pow(ans_div, mod - 2) % mod
    return ans


n, a, b = map(int, input().split())
ans = mod_pow(2, n) - calc_comb(n, a) - calc_comb(n, b) - 1
print(ans % mod)