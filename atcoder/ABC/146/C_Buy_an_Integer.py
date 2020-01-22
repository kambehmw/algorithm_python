A, B, X = map(int, input().split())
if A * (10 ** 9) + B * len(str(10 ** 9)) <= X:
    print(10 ** 9)
    exit()

left, right = 0, 10 ** 9
ans = 0
while (right - left) > 1:
    mid = (left + right) // 2
    if A * mid + B * len(str(mid)) <= X:
        left = mid
        ans = mid
    else:
        right = mid
print(ans)