N, K = map(int, input().split())
x = [0] * N
for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        x[a-1] += 1
ans = 0
for y in x:
    if y == 0:
        ans += 1
print(ans)