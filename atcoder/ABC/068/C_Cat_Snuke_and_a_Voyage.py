N, M = tuple(map(int, input().split()))
A, B = [], []
for _ in range(M):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)
path1 = set()
path2 = set()
for a, b in zip(A, B):
    if a == 1:
        path1.add(b)
    if b == N:
        path2.add(a)
if len(path1.intersection(path2)) > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
