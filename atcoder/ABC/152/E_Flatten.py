# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
lcm_val = A[0]
for a in A[1:]:
    lcm_val = lcm(lcm_val, a)

ans = 0
for a in A:
    ans += lcm_val // a
print(ans % mod)