N, K, M, R = map(int, input().split())
S = [int(input()) for _ in range(N - 1)]
S.sort(reverse=True)
if R <= sum(S[:K]) / K:
    print(0)
    exit()

total = sum(S[:K-1])
X = K * R - total
if M < X:
    print(-1)
    exit()
else:
    print(X)