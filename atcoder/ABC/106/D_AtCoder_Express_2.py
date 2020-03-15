N, M, Q = map(int, input().split())
L, R = [], []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

p, q = [], []
for _ in range(Q):
    tmp = list(map(int, input().split()))
    p.append(tmp[0])
    q.append(tmp[1])

cum_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    cum_sum[L[i]][R[i]] += 1

for i in range(1, N+1):
    for j in range(1, N+1):
        cum_sum[i][j] += cum_sum[i][j-1]
        cum_sum[i][j] += cum_sum[i-1][j]
        cum_sum[i][j] -= cum_sum[i-1][j-1]

def get_sum_range(L, R):
    ans = cum_sum[R][R] - cum_sum[R][L-1] - cum_sum[L-1][R] + cum_sum[L-1][L-1]
    return ans

for i in range(Q):
    ans = get_sum_range(p[i], q[i])
    print(ans)