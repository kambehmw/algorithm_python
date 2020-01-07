A = int(input())
ans = 0
for i in range(1, A):
    x = i
    y = A - x
    ans = max(ans, x * y)
print(ans)
