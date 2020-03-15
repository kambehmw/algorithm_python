S = input()
cnt = 0
x = True
ans = 0
for i in range(len(S)):
    if x:
        if S[i] == "2":
            x = False
        else:
            if 0 < cnt:
                ans += sum(range(1, cnt+1))
                cnt = 0
            else:
                cnt = 0
            x = True
    else:
        if S[i] == "5":
            x = True
            cnt += 1
        else:
            if 0 < cnt:
                ans += sum(range(1, cnt+1))
                cnt = 0
            else:
                cnt = 0
            if S[i] == "2":
                x = False
            else:
                x = True
if 0 < cnt:
    ans += sum(range(1, cnt+1))
print(ans)