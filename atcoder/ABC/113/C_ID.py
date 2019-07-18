N, M = map(int, input().split())
pref_and_year = []
for i in range(M):
    p, y = map(int, input().split())
    pref_and_year.append((p, y))

sorted_indices = sorted(range(len(pref_and_year)),
                        key=lambda k: pref_and_year[k][1])
sorted_perf_and_year = sorted(pref_and_year, key=lambda x: x[1])
count = [0] * N
res = []
for i, x in zip(sorted_indices, sorted_perf_and_year):
    count[x[0]-1] += 1
    auth_number = str(x[0]).zfill(6) + str(count[x[0]-1]).zfill(6)
    res.append((i, auth_number))
res = sorted(res, key=lambda x: x[0])
for x in res:
    print(x[1])

