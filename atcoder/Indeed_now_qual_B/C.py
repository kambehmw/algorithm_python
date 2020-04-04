import heapq
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * N
h = [0]
heapq.heapify(h)
ans = []
while 0 < len(h):
    u = heapq.heappop(h)
    if visited[u]:
        continue

    visited[u] = True
    ans.append(u)
    for v in edges[u]:
        if visited[v]:
            continue

        heapq.heappush(h, v)

ans = [x + 1 for x in ans]
print(*ans)