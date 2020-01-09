N, S, T = tuple(map(int, input().split()))
W = 0
cnt = 0
for _ in range(N):
    W += int(input())
    if S <= W <= T:
        cnt += 1
print(cnt)
