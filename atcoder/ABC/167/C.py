N, M, X = map(int, input().split())
C, A = [], []
for _ in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])

ans = float('inf')
for i in range(2 ** N):
    s = []
    for j in range(N):
        if (i >> j) & 1:
            s.append(j)

    # print(s)
    cost = 0
    score = [0] * M
    for t in s:
        cost += C[t]
        for k, a in enumerate(A[t]):
            score[k] += a
    # print(score)
    flag = True
    for sc in score:
        if sc < X:
            flag = False
            break
    if flag:
        ans = min(ans, cost)

# print(ans)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
