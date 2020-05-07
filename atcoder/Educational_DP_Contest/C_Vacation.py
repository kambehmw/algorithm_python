N = int(input())
A, B, C = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dp = [[0] * 3 for _ in range(N + 5)]
for i in range(3):
    dp[0][i] = 0

for i in range(N):
    dp[i + 1][0] = max(dp[i][1] + A[i], dp[i][2] + A[i])
    dp[i + 1][1] = max(dp[i][0] + B[i], dp[i][2] + B[i])
    dp[i + 1][2] = max(dp[i][0] + C[i], dp[i][1] + C[i])
# print(dp)
ans = 0
for i in range(N + 1):
    for j in range(3):
        ans = max(ans, dp[i][j])
print(ans)