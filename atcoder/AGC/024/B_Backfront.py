N = int(input())
P = [int(input()) for _ in range(N)]
Q = [0] * N
for i in range(N):
    Q[P[i]-1] = i
ans = 0
cnt = 1
for i in range(N-1):
    if Q[i] < Q[i+1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(N - ans)