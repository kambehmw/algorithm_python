N, C, K = tuple(map(int, input().split()))
T = [int(input()) for _ in range(N)]
T = sorted(T)
base = T[0]
count = 1
ans = 1
for i in range(1, N):
    if T[i] <= base + K and count < C:
        count += 1
        continue
    base = T[i]
    count = 1
    ans += 1
print(ans)