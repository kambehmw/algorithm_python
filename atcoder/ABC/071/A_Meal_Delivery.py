x, a, b = tuple(map(int, input().split()))
if abs(x - a) < abs(x - b) :
    print("A")
else:
    print("B")