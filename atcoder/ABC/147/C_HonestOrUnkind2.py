N = int(input())
A = []
xy = []
for _ in range(N):
    a = int(input())
    A.append(a)
    tmp = []
    for _ in range(a):
        tmp.append(tuple(map(int, input().split())))
    xy.append(tmp)
ans = 0
for i in range(2**N)[::-1]:
    is_honest = [0] * N
    for idx, c in enumerate(bin(i)[2:][::-1]):
        if c == "1":
            is_honest[idx] = 1

    flag = True
    for i in range(N):
        a = A[i]
        for j in range(a):
            x, y = xy[i][j][0], xy[i][j][1]
            if is_honest[i]:
                if is_honest[x-1] != y:
                    flag = False
                    break
        if not flag:
            break
    if flag:
        ans = max(ans, sum(is_honest))
print(ans)