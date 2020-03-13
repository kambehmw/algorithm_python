N, D, K = map(int, input().split())
L, R = [], []
for _ in range(D):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
S, T = [], []
for _ in range(K):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)

for s, t in zip(S, T):
    pos = s
    for i, (l, r) in enumerate(zip(L, R), 1):
        if l <= pos <= r:
            if l <= t <= r:
                pos = t
            else:
                if s < t:
                    pos = r
                else:
                    pos = l
        if pos == t:
            print(i)
            break

