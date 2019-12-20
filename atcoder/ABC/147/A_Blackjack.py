A1, A2, A3 = tuple(map(int, input().split()))
if A1 + A2 + A3 <= 21:
    print("win")
else:
    print("bust")