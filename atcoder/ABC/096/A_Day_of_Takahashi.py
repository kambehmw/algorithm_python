a, b = tuple(map(int, input().split()))
if a <= b:
    ans = a
else:
    ans = a - 1
print(ans)