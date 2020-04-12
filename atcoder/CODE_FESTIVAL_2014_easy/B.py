import math
n = int(input())
d = (math.ceil(n / 20) - 1)
if d % 2 == 0:
    if n % 20 == 0:
        print(20)
    else:
        print(n % 20)
else:
    if n % 20 == 0:
        print(1)
    else:
        print(21 - n % 20)