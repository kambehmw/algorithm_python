N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 1
ans = 0
for i in range(N-1):
    if A[i] < A[i + 1]:
        cnt += 1
    else:
        if K <= cnt:
            ans += cnt - K + 1
        cnt = 1
if K <= cnt:
    ans += cnt - K + 1
print(ans)