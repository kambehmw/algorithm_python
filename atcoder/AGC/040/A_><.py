S = input()
N = len(S)
cnts = []
now = "<"
if S[0] == ">":
    cnts.append(0)
    now = ">"
cnt = 0
for i in range(N):
    if S[i] == now:
        cnt += 1
    else:
        cnts.append(cnt)
        cnt = 1
        now = ">" if now == "<" else "<"

if cnt > 0:
    cnts.append(cnt)

if len(cnts) % 2 != 0:
    cnts.append(0)

ans = 0
for i in range(0, len(cnts), 2):
    if cnts[i] < cnts[i+1]:
        ans += sum([x for x in range(cnts[i])])
        ans += sum([x for x in range(cnts[i+1] + 1)])
    else:
        ans += sum([x for x in range(cnts[i] + 1)])
        ans += sum([x for x in range(cnts[i + 1])])
print(ans)
