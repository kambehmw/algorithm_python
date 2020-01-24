import math

EPS = 0.0000000001
PI = math.pi


def f(a, b, theta):
    if theta > PI / 2.0 - EPS:
        return 0.0

    if a * math.tan(theta) <= b:
        ret = a * a * b - a * a * a * math.tan(theta) / 2.0
    else:
        ret = b * b / math.tan(theta) * a / 2.0
    return ret


a, b, x = map(int, input().split())
ok = PI / 2.0
ng = 0.0
for i in range(1, 100001):
    mid = (ok + ng) / 2.0
    if f(a, b, mid) < x:
        ok = mid
    else:
        ng = mid
print(ok / PI * 180)