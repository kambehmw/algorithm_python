C = input()
if C == "a" or C == "zzzzzzzzzzzzzzzzzzzz":
    print("NO")
    exit()

s = set(C)
if "a" in s and len(s) == 1:
    ans = C[:-2] + "b"
    print(ans)
    exit()

if len(C) < 20:
    ans = ""
    flag = True
    for c in C:
        if flag and c != "a":
            ans += chr(ord(c) - 1)
            flag = False
        else:
            ans += c
    ans += "a"
else:
    s = set(C)
    max_ch = max(s)
    min_ch = min(s)
    ans = ""
    flag1 = True
    flag2 = True
    for c in C:
        if flag1 and c == max_ch:
            flag1 = False
            ans += chr(ord(c) - 1)
        elif flag2 and c == min_ch:
            flag2 = False
            ans += chr(ord(c) + 1)
        else:
            ans += c
print(ans)