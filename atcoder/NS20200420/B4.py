import sys
sys.setrecursionlimit(10 ** 6)

n, x = map(int, input().split())
H = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

ans = set()
route = []

def dfs(u, p):
    if p != -1:
        route.append((p, u))
    if H[u] == 1:
        # print(route)
        for x in route:
            ans.add(x)
    for v in edges[u]:
        if v == p:
            continue
        dfs(v, u)

    if 0 < len(route):
        route.pop()

x -= 1
dfs(x, -1)
print(2 * len(ans))