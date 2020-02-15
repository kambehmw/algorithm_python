N, K = map(int, input().split())
P = list(map(int, input().split()))
expects = [0.0]
for i in range(1, 1001):
    p = 0.0
    for j in range(i, 0, -1):
        p += j * 1.0 / i
    expects.append(p)
exp_P = [0.0]
for i in range(N):
    exp_P.append(exp_P[-1] + expects[P[i]])

# print(exp_P)
ans = float('-inf')
for i in range(K, N+1):
    ans = max(ans, exp_P[i] - exp_P[i-K])
print(ans)
