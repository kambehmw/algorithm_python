W = int(input())
N, K = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[[0] * (W + 1) for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        for k in range(1, W + 1):
            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
            if A[i - 1] <= k:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - A[i - 1]] + B[i - 1])
# print(dp)
print(dp[N][K][W])