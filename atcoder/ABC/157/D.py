import sys
sys.setrecursionlimit(10 ** 7)

N, M, K = map(int, input().split())
edges = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].add(b)
    edges[b].add(a)

block_edges = [set() for _ in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    block_edges[c].add(d)
    block_edges[d].add(c)

visited = [False] * N
cnt = 0

def dfs(u, s):
    if visited[u]:
        return

    visited[u] = True
    for v in edges[u]:
        if visited[v]:
            continue
        if v == s:
            continue

        if v in block_edges[s] or v in edges[s]:
            pass
        else:
            global cnt
            cnt += 1

        dfs(v, s)


ans = []
for i in range(N):
    visited = [False] * N
    cnt = 0
    for v in edges[i]:
        dfs(v, i)
    ans.append(cnt)
print(*ans)