n = int(input())
R = [int(input()) for _ in range(n)]
ans = float('-inf')
min_val = R[0]
for r in R[1:]:
    ans = max(ans, r - min_val)
    min_val = min(min_val, r)
print(ans)