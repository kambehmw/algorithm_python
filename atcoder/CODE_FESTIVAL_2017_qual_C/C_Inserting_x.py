s = input()
l, r = 0, len(s) - 1
ans = 0
while l < r:
    # print(l, r)
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        if s[l] == "x":
            l += 1
        elif s[r] == "x":
            r -= 1
        else:
            print(-1)
            exit()
        ans += 1
print(ans)
