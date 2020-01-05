N, Q = tuple(map(int, input().split()))
A = [0] * N
for _ in range(Q):
    l, r, t = tuple(map(int, input().split()))
    l -= 1
    r -= 1
    for i in range(l, r+1):
        A[i] = t
for a in A:
    print(a)
