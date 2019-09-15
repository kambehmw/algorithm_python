N, M = tuple(map(int, input().split()))
A, B = [], []
for _ in range(M):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)
roads = {i: 0 for i in range(1, N+1)}
for a, b in zip(A, B):
    roads[a] += 1
    roads[b] += 1
for key, val in sorted(roads.items()):
    print(val)