A, B, C = tuple(map(int, input().split()))
if (A - B) >= C:
    print(0)
else:
    print(C - (A - B))
