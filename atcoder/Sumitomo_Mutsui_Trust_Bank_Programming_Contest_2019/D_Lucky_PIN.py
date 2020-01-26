N = int(input())
S = input()
c = [str(i) for i in range(10)]
cands = []
for c1 in c:
    for c2 in c:
        for c3 in c:
            cands.append(c1 + c2 + c3)

cnt = 0
for c in cands:
    i = 0
    for s in S:
        if i == 3:
            break
            
        if c[i] == s:
            i += 1

    if i == 3:
        # print(c)
        cnt += 1
print(cnt)