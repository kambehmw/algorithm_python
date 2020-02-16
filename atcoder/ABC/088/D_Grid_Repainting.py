dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(start, goal):
    q = [[start]]
    while len(q) > 0:
        path = q.pop(0)
        n = path[len(path) - 1]
        if n == goal:
            return path
        else:
            for sy, sx in zip(dy, dx):
                py = n[0] + sy
                px = n[1] + sx
                if py < 0 or H <= py:
                    continue
                if px < 0 or W <= px:
                    continue
                if S[py][px] == "#":
                    continue
                if visited[py][px]:
                    continue
                visited[py][px] = True
                x = (py, px)
                if x not in path:
                    new_path = path[:]
                    new_path.append(x)
                    q.append(new_path)
    return None


H, W = map(int, input().split())
S = []
for i in range(H):
    S.append([c for c in input()])
# print(S)
visited = [[False for _ in range(W)] for _ in range(H)]
start = (0, 0)
goal = (H-1, W-1)
ans = bfs(start, goal)
if ans is None:
    print(-1)
    exit()
# print(ans)
counter = 0
for i in range(H):
    for j in range(W):
        if (i, j) in ans:
            continue
        if S[i][j] == ".":
            counter += 1
print(counter)
