def warshall_floyd(d):
    # d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


N, M = map(int, input().split())
d = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = t
    d[b][a] = t
for i in range(N):
    d[i][i] = 0
res = warshall_floyd(d)
# print(res)
ans = float('inf')
for x in res:
    ans = min(ans, max(x))
print(ans)
