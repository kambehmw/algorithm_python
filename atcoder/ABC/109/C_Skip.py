def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


N, X = map(int, input().split())
x = list(map(int, input().split()))
x = [abs(X - e) for e in x]

res = x[0]
for e in x[1:]:
    res = gcd(res, e)
print(res)