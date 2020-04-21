N, M = map(int, input().split())
A = list(map(int, input().split()))
B, C, I = [], [], []
for _ in range(M):
    tmp = list(map(int, input().split()))
    B.append(tmp[0])
    C.append(tmp[1])
    I.append([x - 1 for x in tmp[2:]])

ans = 0
for i in range(2**N):
    unit = set()
    for j in range(N):
        if (i >> j) & 1:
            unit.add(j)

    # print(unit)
    if len(unit) != 9:
        continue

    score = 0
    for b, ic in zip(B, I):
        si = set(ic)
        if 3 <= len(unit.intersection(si)):
            # print(unit)
            score += b

    for j in unit:
        score += A[j]

    ans = max(ans, score)
print(ans)
