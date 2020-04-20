N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for _ in range(N-1)]
ans = 0
for a in A:
    if S <= W <= T:
        ans += 1
    W += a
if S <= W <= T:
    ans += 1
print(ans)