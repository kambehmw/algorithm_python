A, B = tuple(map(int, input().split()))
if A == 1:
    if B == 1:
        print("Draw")
    else:
        print("Alice")
else:
    if B == 1:
        print("Bob")
    else:
        if A < B:
            print("Bob")
        elif A > B:
            print("Alice")
        else:
            print("Draw")