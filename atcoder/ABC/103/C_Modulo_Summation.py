def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(x, y):
    return (x * y) // gcd(x, y)


N = int(input())
A = list(map(int, input().split()))
res = A[0]
for i in range(1, N):
    res = lcm(res, A[i])
res = res - 1
ans = 0
for a in A:
    ans += (res % a)
print(ans)
