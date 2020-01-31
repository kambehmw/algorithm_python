N = int(input())
A = [int(input()) for _ in range(N)]
set_A = set(A)
indices = {a: i for i, a in enumerate(sorted(set_A))}
for a in A:
    print(indices[a])