N = int(input())
S = input()
sn = len(S)
T = [input() for _ in range(N)]
mod = 10 ** 9 + 7
dp = [0] * (sn + 1)
dp[0] = 1
for i in range(1, sn+1):
    for t in T:
        nt = len(t)
        if i - nt < 0:
            continue
        if S[i - nt:i] == t:
            dp[i] += dp[i - nt]
print(dp[sn] % mod)