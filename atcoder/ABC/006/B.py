n = int(input())
A = [0] * (10**6)
mod = 10007
A[0] = 0
A[1] = 0
A[2] = 1
if n > 3:
    for i in range(3, n):
        A[i] = A[i-1] + A[i-2] + A[i-3]
        A[i] %= mod
print(A[n-1] % mod)
