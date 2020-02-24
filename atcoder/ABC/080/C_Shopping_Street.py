N = int(input())
F, P = [], []
for _ in range(N):
    F.append(list(map(int, input().split())))
for _ in range(N):
    P.append(list(map(int, input().split())))

ans = float('-inf')
for i in range(1, 2**10):
    flags = [0] * 10
    for i, c in enumerate(bin(i)[2:][::-1]):
        if c == "1":
            flags[i] = 1

    res = 0
    for f, p in zip(F, P):
        cnt = 0
        for x, y in zip(f, flags):
            if x & y:
                cnt += 1
        res += p[cnt]
    ans = max(ans, res)
print(ans)