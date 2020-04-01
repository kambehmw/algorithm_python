import queue
N = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
M = int(input())
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)

visited = [False] * N
dist = [float('inf')] * N
dp = [0] * N
d = queue.Queue()
mod = 10 ** 9 + 7

dist[a] = 0
dp[a] = 1
d.put(a)
while not d.empty():
    v = d.get()
    if visited[v]:
        continue
    visited[v] = True
    for i in edges[v]:
        to = i
        if dist[to] == float('inf') or dist[to] == dist[v] + 1:
            dp[i] += dp[v]
            dp[i] % mod
            dist[to] = dist[v] + 1
            d.put(to)
print(dp[b] % mod)