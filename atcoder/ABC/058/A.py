a, b, c = tuple(map(int, input().split()))
if b - a == c - b:
    print("YES")
else:
    print("NO")