N = int(input())
C, S, F = [], [], []
for _ in range(N-1):
    c, s, f = tuple(map(int, input().split()))
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N):
    total_time = 0
    for j in range(i, N-1):
        if total_time < S[j]:
            total_time = S[j]
        elif total_time % F[j] == 0:
            pass
        else:
            total_time = total_time + (F[j] - total_time % F[j])
        total_time += C[j]
    print(total_time)
