from collections import defaultdict
N, X, Y = map(int, input().split())
d = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        d[i][j] = d[i][j-1] + 1
X -= 1
Y -= 1
for i in range(N-1):
    for j in range(i + 1, N):
        diff = abs(X - i) + abs(Y - j) + 1
        if diff < d[i][j]:
            d[i][j] = diff
#print(d)
ans = defaultdict(int)
for i in range(N-1):
    for j in range(i + 1, N):
        ans[d[i][j]] += 1
for k in range(1, N):
    print(ans[k])