N = int(input())
A = list(map(int, input().split()))
ans = 0
i = 1
for a in A:
    if a == i:
        i += 1
        ans += 1
if ans == 0:
    print(-1)
else:
    print(N - ans)
