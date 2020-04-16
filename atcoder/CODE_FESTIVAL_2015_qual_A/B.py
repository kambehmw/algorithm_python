N = int(input())
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A, 1):
    ans += 2 ** (N - i) * a
print(ans)