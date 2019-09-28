N, K = tuple(map(int, input().split()))
cnt = [0] * (10**5+1)
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    cnt[a] += b

for i in range(1, 10**5+1):
    if K <= cnt[i]:
        print(i)
        exit()
    K -= cnt[i]
