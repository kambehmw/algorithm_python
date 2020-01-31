import math

N = int(input())
NMAX = 100010
dp = [float('inf')] * NMAX
dp[0] = 0
for i in range(1, N + 1):
    dp[i] = i
    if i >= 6:
        for j in range(1, int(math.log(NMAX, 6)) + 1):
            dp[i] = min(dp[i], dp[i - 6 ** j] + 1)

    if i >= 9:
        for j in range(1, int(math.log(NMAX, 9)) + 1):
            dp[i] = min(dp[i], dp[i - 9 ** j] + 1)
# print(dp)
print(dp[N])
