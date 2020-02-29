H, W = map(int, input().split())
A = []
for h in range(H):
    tmp = list(map(int, input().split()))
    if h % 2 == 0:
        r = range(W)
    else:
        r = range(W)[::-1]

    for w in r:
        A.append((h, w, tmp[w]))

ans = []
for i in range(len(A) - 1):
    if A[i][2] % 2 != 0:
        ans.append((A[i][0] + 1, A[i][1] + 1, A[i + 1][0] + 1, A[i + 1][1] + 1))
        A[i + 1] = (A[i + 1][0], A[i + 1][1], A[i + 1][2] + 1)
print(len(ans))
for x in ans:
    print(*x)
