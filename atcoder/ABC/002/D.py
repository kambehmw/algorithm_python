from itertools import combinations
N, M = map(int, input().split())
edges = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x][y] = True
    edges[y][x] = True

for num in range(N, 0, -1):
    for e in combinations(range(N), num):
        flag = True
        for i, j in combinations(e, 2):
            if not edges[i][j]:
                flag = False
                break
        if flag:
            print(num)
            exit()
print(1)