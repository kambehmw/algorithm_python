import math
N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = tuple(map(int, input().split()))
    X.append(x)
    Y.append(y)

ans = float('-inf')
for i in range(N-1):
    for j in range(i+1, N):
        dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
        dist = math.sqrt(dist)
        ans = max(ans, dist)
print(ans)