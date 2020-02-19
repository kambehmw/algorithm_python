stack = []

def dfs(visited):
    while 0 < len(stack):
        v = stack.pop()
        for i, u in enumerate(edges[v]):
            if u is True:
                if visited[i]:
                    continue
                visited[i] = True
                stack.append(i)
                dfs(visited)


N, M = tuple(map(int, input().split()))
edges = [[False for _ in range(N)] for _ in range(N)]
A, B = [], []
for i in range(M):
    a, b = tuple(map(int, input().split()))
    a -= 1
    b -= 1
    edges[a][b] = True
    edges[b][a] = True
    A.append(a)
    B.append(b)

ans = 0
for a, b in zip(A, B):
    edges[a][b] = False
    edges[b][a] = False
    visited = [False] * N
    cnt = 0
    for v in range(N):
        if visited[v]:
            continue
        cnt += 1
        visited[v] = True
        stack.append(v)
        dfs(visited)
    if 1 < cnt:
        ans += 1
    edges[a][b] = True
    edges[b][a] = True
print(ans)