N, K = map(int, input().split())
A = list(map(int, input().split()))
partial_sum = [0] * (N + 1)
for i in range(N):
    partial_sum[i+1] = partial_sum[i] + A[i]
# print(partial_sum)
total = 0
for i in range(N-K+1):
    total += partial_sum[i+K] - partial_sum[i]
print(total)