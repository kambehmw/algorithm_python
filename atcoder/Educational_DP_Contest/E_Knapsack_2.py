N, W = map(int, input().split())
wt, vt = [], []
for _ in range(N):
    w, v = map(int, input().split())
    wt.append(w)
    vt.append(v)

dp = [[float('inf')] * (10 ** 5 + 5) for _ in range(N + 5)]
dp[0][0] = 0
for i in range(N):
    for j in range(10 ** 5 + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if 0 <= j - vt[i]:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - vt[i]] + wt[i])
# print(dp)
ans = 0
for i in range(N + 1):
    for j in range(10 ** 5 + 1):
        if dp[i][j] <= W:
            ans = max(ans, j)
print(ans)