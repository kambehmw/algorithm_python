N = int(input())
X = list(map(int, input().split()))
ans = float('inf')
for i in range(1, 101):
    total = 0
    for j in range(N):
        total += (i - X[j]) ** 2
    ans = min(ans, total)
print(ans)