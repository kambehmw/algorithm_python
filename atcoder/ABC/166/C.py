N, M = map(int, input().split())
H = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(u, p=-1):
    for v in edges[u]:
        if v == p:
            continue
        if H[u] <= H[v]:
            return False
        dfs(v, u)
    return True

ans = 0
for i in range(N):
    if dfs(i, -1):
        ans += 1
print(ans)