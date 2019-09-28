N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    if x < abs(x - K):
        ans += 2 * x
    else:
        ans += 2 * abs(x - K)
print(ans)