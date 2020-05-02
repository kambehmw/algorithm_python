import sys
sys.setrecursionlimit(10 ** 6)
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for _ in range(Q):
    ta, tb, tc, td = map(int, input().split())
    ta -= 1
    tb -= 1
    a.append(ta)
    b.append(tb)
    c.append(tc)
    d.append(td)

x = []
def dfs(s):
    if len(s) - s.count("0") == N:
        x.append(s)
        return

    if s[-1] == "0":
        start = 10
    else:
        start = s[-1]
    for i in range(int(start), M+1):
        dfs(s + str(i))
        # x.append(res)

ans = 0
for i in range(1, M+1):
    x = []
    dfs(str(i))
    # print(x)
    for y in x:
        A = []
        for z in y:
            if z == "0":
                A[-1] += z
            else:
                A.append(z)
        A = [int(z) for z in A]
        # print(A)
        score = 0
        for ta, tb, tc, td in zip(a, b, c, d):
            if A[int(tb)] - A[int(ta)] == tc:
                score += td
        ans = max(ans, score)
print(ans)
