S = input()
N = len(S)
S = S.lower()
cnt = 0
for i in range(N):
    if cnt == 0:
        if S[i] == "i":
            cnt += 1
    elif cnt == 1:
        if S[i] == "c":
            cnt += 1
    elif cnt == 2:
        if S[i] == "t":
            cnt += 1
if cnt == 3:
    print("YES")
else:
    print("NO")