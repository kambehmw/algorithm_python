import queue

que = queue.Queue()
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(visited, dists):
    while not que.empty():
        y, x, counter = que.get()
        for sy, sx in zip(dy, dx):
            py = y + sy
            px = x + sx
            if visited[py][px]:
                continue
            if maze[py][px] == "#":
                continue
            que.put((py, px, counter+1))
            visited[py][px] = True
            dists[py][px] = counter+1


R, C = tuple(map(int, input().split()))
sy, sx = tuple(map(int, input().split()))
gy, gx = tuple(map(int, input().split()))
maze = []
for _ in range(R):
    maze.append([c for c in input()])

visited = [[False for _ in range(C)] for _ in range(R)]
dists = [[-1 for _ in range(C)] for _ in range(R)]
counter = 0
sy -= 1
sx -= 1
que.put((sy, sx, counter))
visited[sy][sx] = True
dists[sy][sx] = counter
bfs(visited, dists)
print(dists[gy-1][gx-1])