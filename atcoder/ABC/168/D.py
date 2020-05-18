from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

rooms = [-1] * N
def bfs(u):
    q = deque()
    q.append(u)
    while 0 < len(q):
        v = q.popleft()
        for e in edges[v]:
            if rooms[e] == -1:
                rooms[e] = v + 1
                q.append(e)

bfs(0)
print("Yes")
print(*rooms[1:], sep="\n")
