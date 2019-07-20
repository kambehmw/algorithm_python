import itertools

N, M = list(map(int, input().split()))
K, S = [], []
for _ in range(M):
    temp = list(map(int, input().split()))
    K.append(temp[0])
    S.append(temp[1:])

P = list(map(int, input().split()))

ans = 0
for x in itertools.product(("on", "off"), repeat=N):
    flag = True
    for s, p in zip(S, P):
        count = 0
        for i in s:
            if x[i-1] == "on":
                count += 1
        if count % 2 != p:
            flag = False
    if flag:
        ans += 1
print(ans)
