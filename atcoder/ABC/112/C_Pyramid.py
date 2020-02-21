N = int(input())
X, Y, H = [], [], []
target = (-1, -1, -1)
for _ in range(N):
    x, y, h = map(int, input().split())
    X.append(x)
    Y.append(y)
    H.append(h)
    if h >= 1:
        target = (x, y, h)

for cx in range(101):
    for cy in range(101):
        v = target[2] + abs(target[0] - cx) + abs(target[1] - cy)
        v = max(v, 0)
        flag = True
        for x, y, h in zip(X, Y, H):
            vv = v - abs(x - cx) - abs(y - cy)
            vv = max(vv, 0)
            if h != vv:
                flag = False
                break
        if flag:
            print(cx, cy, v)
            exit()