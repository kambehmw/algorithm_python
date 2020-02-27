from collections import deque

H, W = map(int, input().split())
A = []
D = [[-1 for _ in range(W)] for _ in range(H)]
q = deque([])
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == "#":
            q.append((i, j))
            D[i][j] = 0
    A.append(S)

while q:
    pos = q.popleft()
    py, px = pos[0], pos[1]
    for (y, x) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ny = py + y
        nx = px + x
        if nx < 0 or W <= nx or ny < 0 or H <= ny:
            continue
        if D[ny][nx] < 0:
            D[ny][nx] = D[py][px] + 1
            q.append((ny, nx))

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, D[i][j])
print(ans)
