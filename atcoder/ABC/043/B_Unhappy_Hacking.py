s = input()
ans = ""
for c in s:
    if c == "0":
        ans += "0"
    elif c == "1":
        ans += "1"
    elif c == "B":
        ans = ans[:-1]
print(ans)