import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    max_dist = 0
    while not que.empty():
        pos = que.get()
        for y, x in zip(dy, dx):
            ty = pos[0] + y
            tx = pos[1] + x
            if ty < 0 or H <= ty:
                continue
            if tx < 0 or W <= tx:
                continue
            if visited[ty][tx]:
                continue
            if S[ty][tx] == "#":
                continue
            que.put((ty, tx, pos[2] + 1))
            visited[ty][tx] = True
            max_dist = max(max_dist, pos[2] + 1)
    return max_dist


H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append([c for c in input()])
ans = 0
for sy in range(H):
    for sx in range(W):
        if S[sy][sx] == "#":
            continue
        visited = [[False for _ in range(W)] for _ in range(H)]
        visited[sy][sx] = True
        que = queue.Queue()
        que.put((sy, sx, 0))
        ans = max(ans, bfs())
print(ans)