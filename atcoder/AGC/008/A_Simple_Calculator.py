x, y = tuple(map(int, input().split()))
if x == y:
    print(0)
    exit()

if abs(x) == abs(y):
    print(1)
    exit()

if 0 <= x:
    if x <= y:
        print(y - x)
    else:
        if abs(x) < abs(y):
            print(abs(y) - abs(x) + 1)
        else:
            if 0 < y:
                print(abs(x - y) + 2)
            else:
                print(x - abs(y) + 1)
else:
    if y < x:
        print(abs(x - y) + 2)
    else:
        if abs(y) < abs(x):
            if 0 < y:
                print(abs(x) - y + 1)
            else:
                print(y - x)
        else:
            print(abs(abs(x) - y) + 1)
