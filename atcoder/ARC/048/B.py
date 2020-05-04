N = int(input())
R, H = [], []
for _ in range(N):
    r, h = map(int, input().split())
    R.append(r)
    H.append(h)

d = {}
for i, r in enumerate(R):
    if r not in d:
        d[r] = {"A": [], "B": [], "C": []}
    if H[i] == 1:
        d[r]["A"].append(i)
    elif H[i] == 2:
        d[r]["B"].append(i)
    elif H[i] == 3:
        d[r]["C"].append(i)

K = 0
ans = [None] * N
for k, v in sorted(d.items()):
    A, B, C = len(v["A"]), len(v["B"]), len(v["C"])
    for a in v["A"]:
        ans[a] = (K + B, N - K - A - B, A - 1)
    for b in v["B"]:
        ans[b] = (K + C, N - K - B - C, B - 1)
    for c in v["C"]:
        ans[c] = (K + A, N - K - C - A, C - 1)
    K += (A + B + C)
for x in ans:
    print(*x)