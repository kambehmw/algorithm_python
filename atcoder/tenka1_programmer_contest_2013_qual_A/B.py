N = int(input())
cnt = 0
for _ in range(N):
    ps = list(map(int, input().split()))
    s = sum(ps)
    if 0 <= s < 20:
        cnt += 1
print(cnt)