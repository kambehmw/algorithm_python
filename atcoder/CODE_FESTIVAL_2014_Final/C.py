A = int(input())
for k in range(10, 10001):
    x = A
    ans = ""
    while 0 < x:
        m = x % k
        ans = str(m) + ans
        x //= k
    # print(k, ans)
    if int(ans) == k:
        print(k)
        exit()
print(-1)