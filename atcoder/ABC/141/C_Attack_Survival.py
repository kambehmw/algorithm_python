N, K, Q = tuple(map(int, input().split()))
A = [int(input()) for _ in range(Q)]
points = [0] * N
for a in A:
    points[a-1] += 1
for p in points:
    if K - (Q - p) > 0:
        print("Yes")
    else:
        print("No")