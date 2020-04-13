N = int(input())
S = input()
dp = [[0] * 105 for _ in range(105)]
ans = float('inf')
for i in range(N):
    s1, s2 = S[:i], S[i:]
    n, m = len(s1), len(s2)
    for j in range(n):
        for k in range(m):
            if s1[j] == s2[k]:
                dp[j + 1][k + 1] = dp[j][k] + 1
            else:
                dp[j + 1][k + 1] = max(dp[j][k + 1], dp[j + 1][k])
    ans = min(ans, N - 2 * dp[n][m])
print(ans)