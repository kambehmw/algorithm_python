N, X = tuple(map(int, input().split()))
M = [int(input()) for _ in range(N)]
min_val = min(M)
X = X - sum(M)
print(N + X // min_val)