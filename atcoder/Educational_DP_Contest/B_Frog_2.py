N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [float('inf')] * (N + K + 5)
dp[0] = 0
for i in range(N):
    for k in range(1, K + 1):
        if i + k < N:
            dp[i + k] = min(dp[i + k], dp[i] + abs((H[i] - H[i + k])))
# print(dp)
print(dp[N - 1])
