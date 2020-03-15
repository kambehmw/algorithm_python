import math
l = list(map(int, input().split()))
l.sort()
if max(l) <= sum(l[:-1]):
    print(math.pi * sum(l) ** 2)
else:
    print(math.pi * (sum(l) ** 2 - (max(l) - sum(l[:-1])) ** 2))