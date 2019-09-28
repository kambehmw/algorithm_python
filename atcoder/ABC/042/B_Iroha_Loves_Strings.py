N, L = tuple(map(int, input().split()))
S = [input() for _ in range(N)]
S = sorted(S)
print("".join(S))