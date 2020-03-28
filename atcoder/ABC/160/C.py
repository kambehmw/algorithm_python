K, N = map(int, input().split())
A = list(map(int, input().split()))
max_diff = 0
for i in range(N-1):
    max_diff = max(max_diff, A[i + 1] - A[i])
max_diff = max(max_diff, K - A[-1] + A[0])
print(K - max_diff)