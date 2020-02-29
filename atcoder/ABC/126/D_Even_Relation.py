import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
visited = [False] * N
colors = [-1] * N
dist = [float('inf')] * N

def dfs(u):
    if visited[u]:
        return

    visited[u] = True
    for (v, w) in edges[u]:
        if visited[v]:
            continue
        if colors[v] != -1:
            continue

        dist[v] = dist[u] + w
        if dist[v] % 2 == 0:
            colors[v] = 0
        else:
            colors[v] = 1
        dfs(v)


edges = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))


colors[0] = 0
dist[0] = 0
dfs(0)
for c in colors:
    print(c)