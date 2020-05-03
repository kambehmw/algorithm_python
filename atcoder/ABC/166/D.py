X = int(input())
for A in range(-118, 120):
    for B in range(-119, 119):
        if 1 <= pow(A, 5) - pow(B, 5) and A - B >= 1:
            if pow(A, 5) - pow(B, 5) == X:
                print(A, B)
                exit()