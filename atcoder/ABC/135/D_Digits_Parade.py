S = input()
dp = [[0] * 13 for _ in range(10 ** 5 + 5)]
MOD = 10 ** 9 + 7
dp[0][0] = 1
n = len(S)
for i in range(n):
    if S[i] == "?":
        c = -1
    else:
        c = int(S[i])

    for j in range(10):
        if c != -1 and c != j:
            continue
        for ki in range(13):
            dp[i + 1][(ki * 10 + j) % 13] += dp[i][ki]

    for j in range(13):
        dp[i + 1][j] %= MOD

print(dp[n][5])
