A, B, C, K = list(map(int, input().split()))
if abs(A - B) > 10**18:
    print("Unfair")
else:
    if K % 2 == 0:
        print(A - B)
    else:
        print(B - A)