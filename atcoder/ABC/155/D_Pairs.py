def ok():
    tot = 0
    for i in range(N):
        if A[i] < 0:
            l, r = -1, N
            while l + 1 < r:
                c = (l + r) // 2
                if A[c] * A[i] < x:
                    r = c
                else:
                    l = c
            tot += N - r
        else:
            l, r = -1, N
            while l + 1 < r:
                c = (l + r) // 2
                if A[c] * A[i] < x:
                    l = c
                else:
                    r = c
            tot += r
        if A[i] * A[i] < x:
            tot -= 1
    tot //= 2
    return tot < K


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
INF = 10 ** 18 + 1
l, r = -INF, INF
while l + 1 < r:
    x = (l + r) // 2
    if ok():
        l = x
    else:
        r = x
print(l)
