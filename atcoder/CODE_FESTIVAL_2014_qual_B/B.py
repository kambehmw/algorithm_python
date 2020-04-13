N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
tot = 0
for i, a in enumerate(A, 1):
    tot += a
    if K <= tot:
        print(i)
        exit()