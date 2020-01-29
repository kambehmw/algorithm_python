N = int(input())
X = []
for _ in range(N):
    x = input()
    X.append([c for c in x])
cnt = 0
prev = None
for y in range(N):
    for x in range(9):
        if y == 0:
            if X[y][x] == "o" or X[y][x] == "x":
                cnt += 1
        else:
            if X[y][x] == "x":
                cnt += 1
            elif X[y][x] == "o":
                if X[y-1][x] != "o":
                    cnt += 1
print(cnt)