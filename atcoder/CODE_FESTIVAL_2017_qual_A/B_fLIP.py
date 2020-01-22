N, M, K = map(int, input().split())
for k in range(N+1):
    for l in range(M+1):
        blacks = k * (M - l) + l * (N - k)
        if blacks == K:
            print("Yes")
            exit()
print("No")