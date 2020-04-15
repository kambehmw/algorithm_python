S = input().split()
ans = set()
for w in S:
    flag = False
    t = ""
    for c in w:
        if c == "@":
            if not flag:
                flag = True
            else:
                if 0 < len(t):
                    ans.add(t)
                t = ""
        else:
            if flag:
                t += c
    if flag:
        if 0 < len(t):
            ans.add(t)

ans = list(ans)
ans.sort()
for x in ans:
    print(x)