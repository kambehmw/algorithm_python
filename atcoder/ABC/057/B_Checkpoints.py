N, M = tuple(map(int, input().split()))
A, B = [], []
for i in range(N):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)
C, D = [], []
for i in range(M):
    c, d = tuple(map(int, input().split()))
    C.append(c)
    D.append(d)
ans = [0] * N
for i, (a, b) in enumerate(zip(A, B)):
    min_diff = float('inf')
    for idx, (c, d) in enumerate(zip(C, D), 1):
        diff = abs(a - c) + abs(b - d)
        if diff < min_diff:
            ans[i] = idx
            min_diff = diff
for x in ans:
    print(x)