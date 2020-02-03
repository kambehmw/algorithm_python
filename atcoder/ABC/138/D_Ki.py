import sys
input = sys.stdin.readline #for input speed
sys.setrecursionlimit(10**6) #for deep recursion
N, Q = map(int, input().split())
to = [[] for _ in range(N)]
ans = [0 for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x

def dfs(v, p=-1):
    for u in to[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v)

dfs(0, -1)
print(*ans)