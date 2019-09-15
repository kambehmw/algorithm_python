# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
T = [int(input()) for _ in range(N)]
if N == 1:
    print(T[0])
    exit()

base = lcm(T[0], T[1])
for i in range(2, N):
    base = lcm(base, T[i])
print(base)
