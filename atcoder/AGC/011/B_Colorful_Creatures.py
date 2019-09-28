N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
ans = 0
for i in range(N-1):
    if A[i+1] > A[i] * 2:
        ans = i + 1
    A[i+1] = A[i] + A[i+1]
print(N - ans)
