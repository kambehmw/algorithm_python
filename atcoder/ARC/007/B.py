N, M = map(int, input().split())
ds = [int(input()) for _ in range(M)]
cd = 0
cases = [x for x in range(1, N+1)]
for d in ds:
    if d not in cases:
        continue
    cases[cases.index(d)], cd = cd, cases[cases.index(d)]
for x in cases:
    print(x)