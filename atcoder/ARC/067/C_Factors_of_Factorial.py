N = int(input())
memo = [0] * (N + 1)

def factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            memo[i] += cnt
        i += 1
    if n > 1:
        memo[n] += 1

for n in range(2, N + 1):
    factor(n)

mod = 10 ** 9 + 7
ans = 1
for m in memo:
    if m >= 1:
        ans *= m + 1
        ans %= mod
print(ans)
