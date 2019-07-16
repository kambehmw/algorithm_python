def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
else:
    res = gcd(A[0], A[1])
    for i in range(2, N):
        res = gcd(res, A[i])
    print(res)