def main():
    N, M = list(map(int, input().split()))
    A = set()
    for i in range(M):
        A.add(int(input()))

    mod = 1000000007

    dp = [0] * (N+1)
    dp[0] = 1
    for now in range(0, N):
        for next in range(now+1, min(N, now+2)+1):
            if next not in A:
                dp[next] += dp[now]
                dp[next] %= mod

    print(dp[N] % mod)

if __name__ == '__main__':
    main()