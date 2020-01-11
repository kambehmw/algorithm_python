A, B, C, D, E, F = tuple(map(int, input().split()))
max_con = 0
res = (100 * A, 0)
for i in range(F // (100 * A) + 1):
    for j in range(F // (100 * B) + 1):
        if i == 0 and j == 0:
            continue
        wat = (A * i + B * j)
        x = 100 * wat
        if F < x:
            continue
        for k in range(wat * E // C + 1):
            for l in range(wat * E // D + 1):
                y = C * k + D * l
                if wat * E < y:
                    continue
                total = x + y
                if F < total:
                    continue
                if max_con < y / total:
                    max_con = y / total
                    res = (total, y)
                    # print(x + y, y)
print(*res)
