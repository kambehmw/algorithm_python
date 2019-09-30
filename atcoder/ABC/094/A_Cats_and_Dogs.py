A, B, X = tuple(map(int, input().split()))
if A <= X <= A + B:
    print("YES")
else:
    print("NO")