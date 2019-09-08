N, M = map(int, input().split())
X, Y = [], []
for i in range(M):
    tmp = list(map(int, input().split()))
    X.append(tmp[0])
    Y.append(tmp[1])
box_ball = [1] * N
red = [False] * N
red[0] = True
for x, y in zip(X, Y):
    if red[x-1]:
        red[y-1] = True
    box_ball[x-1] -= 1
    box_ball[y-1] += 1
    if box_ball[x-1] == 0:
        red[x-1] = False
print(red.count(True))
