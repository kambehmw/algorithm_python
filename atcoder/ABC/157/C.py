N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

for i in range(1000):
    str_i = str(i)
    if len(str_i) != N:
        continue

    flag = True
    for s, c in zip(S, C):
        if int(str_i[s-1]) != c:
            flag = False
            break

    if flag:
        print(i)
        exit()
print(-1)