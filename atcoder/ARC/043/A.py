N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]
D = max(S) - min(S)
if D == 0:
    print(-1)
else:
    P = B / D
    E = sum(S) / N
    Q = A - E * P
    print(P, Q)