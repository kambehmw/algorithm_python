N, T = map(int, input().split())
c, t = [], []
for i in range(N):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    t.append(tmp[1])

res = []
for x, y in zip(c, t):
    if y <= T:
        res.append(x)
if len(res) > 0:
    print(min(res))
else:
    print("TLE")