N, M = map(int, input().split())
B = []
for _ in range(N):
    b = [int(x) for x in input()]
    B.append(b)

ans = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if n == 0 or n == N - 1 or m == 0 or m == M - 1:
            ans[n][m] = 0
            continue

        res = float('inf')
        for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            py = n + y
            px = m + x
            res = min(res, B[py][px])
        ans[n][m] = res

        for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            py = n + y
            px = m + x
            B[py][px] -= res

for x in ans:
    print("".join(map(str, x)))