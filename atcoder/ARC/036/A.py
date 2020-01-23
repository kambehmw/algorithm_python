N, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
for i, x in enumerate(range(2, N), 3):
    total_time = T[x] + T[x-1] + T[x-2]
    if total_time < K:
        print(i)
        exit()
print(-1)