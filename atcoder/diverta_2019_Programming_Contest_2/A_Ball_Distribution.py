N, K = tuple(map(int, input().split()))
if K == 1:
    print(0)
else:
    print(N - (K - 1) - 1)