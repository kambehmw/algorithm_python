N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        jy, jx = Y[j] - Y[i], X[j] - X[i]
        for k in range(j+1, N):
            ky, kx = Y[k] - Y[i], X[k] - X[i]
            area = abs(jx * ky - kx * jy)
            if area % 2 == 0 and area // 2 > 0:
                ans += 1
print(ans)