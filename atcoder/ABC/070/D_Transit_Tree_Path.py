import sys

sys.setrecursionlimit(10 ** 7)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

depth = [0] * N

def dfs(v, p, d):
    depth[v] = d
    for e in edges[v]:
        if e[0] == p:
            continue
        dfs(e[0], v, d + e[1])


Q, K = map(int, input().split())
K -= 1

dfs(K, -1, 0)

for i in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(depth[x] + depth[y])

