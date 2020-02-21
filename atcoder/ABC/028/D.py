N, K = map(int, input().split())
print(((N - K) * (K - 1) * 6 + (N - K) * 3 + (K - 1) * 3 + 1) / (N ** 3))