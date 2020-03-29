def judge_ientersected(ax, ay, bx, by, cx, cy, dx, dy):
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

    return tc * td < 0 and ta * tb < 0


Ax, Ay, Bx, By = map(int, input().split())
N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

cnt = 0
for i in range(N):
    if i == N - 1:
        if judge_ientersected(Ax, Ay, Bx, By, X[i], Y[i], X[0], Y[0]):
            cnt += 1
    else:
        if judge_ientersected(Ax, Ay, Bx, By, X[i], Y[i], X[i + 1], Y[i + 1]):
            cnt += 1
print(cnt // 2 + 1)
