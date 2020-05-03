from copy import deepcopy
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])

ans = 0
def dfs(A):
    global ans
    if len(A) == N + 1:
        now = 0
        for i in range(Q):
            if A[b[i]] - A[a[i]] == c[i]:
                now += d[i]
        ans = max(ans, now)
        return

    A.append(A[-1])
    while A[-1] <= M:
        dfs(deepcopy(A))
        A[-1] += 1

dfs([1])
print(ans)