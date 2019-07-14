a, b = map(int, input().split())
if a <= 0 <= b:
    print("Zero")
    exit()
if 0 < a:
    print("Positive")
    exit()

if b < 0:
    diff = abs(b - a) + 1
    if diff % 2 == 0:
        print("Positive")
    else:
        print("Negative")