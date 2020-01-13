N, M = tuple(map(int, input().split()))
P, S = [], []
for _ in range(M):
    p, s = input().split()
    P.append(int(p))
    S.append(s)

accepted = [False] * N
wrong = [0] * N
AC, WA = 0, 0
for p, s in zip(P, S):
    if s == "WA":
        if not accepted[p-1]:
            wrong[p-1] += 1
    elif s == "AC" and accepted[p-1] is False:
        accepted[p-1] = True
        AC += 1
        WA += wrong[p-1]
print(AC, WA)
