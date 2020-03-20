N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

visited = [False] * N
parents = [-1] * N
flag = True

def dfs(u):
    visited[u] = True
    for v in edges[u]:
        if visited[v]:
            # print(u, parents[u], v)
            if parents[u] != v:
                global flag
                flag = False
            continue
        parents[v] = u
        dfs(v)


ans = 0
for u in range(N):
    if visited[u]:
        continue
    flag = True
    dfs(u)
    if flag:
        ans += 1
print(ans)
