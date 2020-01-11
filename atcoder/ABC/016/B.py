A, B, C = tuple(map(int, input().split()))
if A + B == C:
    if A - B == C:
        print("?")
    else:
        print("+")
elif A - B == C:
    print("-")
else:
    print("!")