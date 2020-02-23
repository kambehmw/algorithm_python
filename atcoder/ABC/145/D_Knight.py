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


X, Y = map(int, input().split())
if (X + Y) % 3 != 0:
    print(0)
    exit()
n = (2 * X - Y) // 3
m = (- X + 2 * Y) // 3
if n < 0 or m < 0:
    print(0)
    exit()
print(calc_comb(n + m, n))
