import math
txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

limit_total = T * V
for x, y in zip(X, Y):
    dist = math.sqrt((x - txa) ** 2 + (y - tya) ** 2)
    dist += math.sqrt((txb - x) ** 2 + (tyb - y) ** 2)
    if dist <= limit_total:
        print("YES")
        exit()
print("NO")