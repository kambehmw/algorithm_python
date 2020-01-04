H1, W1 = tuple(map(int, input().split()))
H2, W2 = tuple(map(int, input().split()))
if H1 == H2 or H1 == W2 or W1 == H2 or W1 == W2:
    print("YES")
else:
    print("NO")