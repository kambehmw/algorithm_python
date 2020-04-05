from bisect import bisect_right
N = int(input())
S =[int(input()) for _ in range(N)]
max_s = max(S)
Q = int(input())
K = [int(input()) for _ in range(Q)]
MAX_S = (10 ** 6 + 5)
cnts = [0] * MAX_S
for s in S:
    cnts[s] += 1
res = [0] * MAX_S
for i in range(MAX_S - 2, -1, -1):
    res[i] = res[i + 1] + cnts[i]
# print(res[:N])
res = [x for x in res if 0 < x]
res = res[::-1]
# print(res)
for i in range(Q):
    k = K[i]
    if N - cnts[0] <= k:
        print(0)
    else:
        idx = bisect_right(res, k)
        print(max_s + 1 - idx)