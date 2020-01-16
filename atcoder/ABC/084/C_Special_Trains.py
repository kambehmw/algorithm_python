N = int(input())
C, S, F = [], [], []
for _ in range(N-1):
    c, s, f = tuple(map(int, input().split()))
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N-1):
    total_time = 0
    for j, (c, s, f) in enumerate(zip(C[i:], S[i:], F[i:])):
        if j == 0:
            total_time += (c + s)
        else:
            if total_time < s:
                total_time = s
            if total_time % f != 0:
                total_time += f - total_time % f
            total_time += c
    print(total_time)
print(0)
