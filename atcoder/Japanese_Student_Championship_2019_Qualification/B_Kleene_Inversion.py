N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
counter = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            counter += 1

counter2 = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            counter2 += 1

ans = 0
ans += counter * K
ans += counter2 * (K * (K - 1) // 2)
print(ans % mod)
