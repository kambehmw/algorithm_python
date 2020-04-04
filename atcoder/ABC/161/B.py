N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
total = sum(A)
ans = 0
for a in A:
    if total <= a * (4 * M):
        ans += 1
if ans >= M:
    print("Yes")
else:
    print("No")