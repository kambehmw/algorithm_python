N = int(input())
S = []
for _ in range(N):
    S.append([c for c in input()])
for x in range(N):
    for y in range(N-1, -1, -1):
        print(S[y][x], end="")
    print()
