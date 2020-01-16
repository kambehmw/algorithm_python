N, A, B = tuple(map(int, input().split()))
i = 0
while N > 0:
    if i % 2 == 0:
        N -= A
    else:
        N -= B

    if N <= 0:
        if i % 2 == 0:
            print("Ant")
        else:
            print("Bug")
    i += 1