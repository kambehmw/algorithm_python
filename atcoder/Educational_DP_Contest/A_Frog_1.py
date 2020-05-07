N = int(input())
H = list(map(int, input().split()))
dp = [float('inf')] * (N + 3)
dp[0] = 0
for i in range(1, N):
    if 0 <= i - 2:
        dp[i] = min(dp[i], dp[i - 2] + abs(H[i] - H[i - 2]))
    dp[i] = min(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]))
# print(dp)
print(dp[N - 1])