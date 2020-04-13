N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
if N < M:
    print("NO")
    exit()

n, m = 0, 0
while m < M and n < N:
    if B[m] <= A[n]:
        m += 1
    n += 1
if m == M:
    print("YES")
else:
    print("NO")