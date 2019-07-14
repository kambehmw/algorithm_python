A, B = map(int, input().split())
ans = 0
for s in range(A, B+1):
    str_s = str(s)
    if str_s == str_s[::-1]:
        ans += 1
print(ans)