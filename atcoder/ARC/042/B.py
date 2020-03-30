import math

def calc_slope_intersept(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)

x, y = map(int, input().split())
N = int(input())
X, Y = [], []
for _ in range(N):
    tx, ty = map(int, input().split())
    X.append(tx)
    Y.append(ty)
ans = float('inf')
for i in range(N):
    x1, y1 = X[i], Y[i]
    if i + 1 == N:
        x2, y2 = X[0], Y[0]
    else:
        x2, y2 = X[i + 1], Y[i + 1]
    if x1 == x2:
        ans = min(ans, abs(x - x1))
    elif y1 == y2:
        ans = min(ans, abs(y - y1))
    else:
        a, b = calc_slope_intersept(x1, y1, x2, y2)
        d = abs(- a * x + y - b) / math.sqrt(a ** 2 + 1)
        ans = min(ans, d)
print(ans)