N, W = map(int, input().split())
wt, vt = [], []
for _ in range(N):
    w, v = map(int, input().split())
    wt.append(w)
    vt.append(v)

dp = [[0] * (W + 5) for _ in range(105)]

for i in range(N):
    for j in range(W + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if 0 <= j - wt[i]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - wt[i]] + vt[i])
# print(dp)
print(dp[N][W])