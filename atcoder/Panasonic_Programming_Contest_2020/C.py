import math
a, b, c = map(int, input().split())
if 4 * a * b < (c - a - b) ** 2 and math.ceil(2 * math.sqrt(a * b)) <= (c - a - b):
    print("Yes")
else:
    print("No")