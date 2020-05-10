N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]
D = 60
MAX_N = 200005
to = [[0] * MAX_N for _ in range(D)]
for i, a in enumerate(A):
    to[0][i] = a

for i in range(D - 1):
    for j in range(N):
        to[i + 1][j] = to[i][to[i][j]]

v = 0
for i in range(D - 1, -1, -1):
    l = 1 << i
    if l <= K:
        v = to[i][v]
        K -= l
print(v + 1)