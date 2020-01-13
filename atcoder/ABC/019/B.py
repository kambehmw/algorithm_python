s = input()
prev = s[0]
cnt = 0
ans = ""
for c in s:
    if prev == c:
        cnt += 1
    else:
        ans += prev + str(cnt)
        prev = c
        cnt = 1
ans += prev + str(cnt)
print(ans)