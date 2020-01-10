import math
N = int(input())
R = [int(input()) for _ in range(N)]
R.sort(reverse=True)
area = 0.0
for i in range(N):
    circle_area = math.pi * (R[i] ** 2)
    if i % 2 == 0:
        pass
    else:
        circle_area *= -1
    area += circle_area
print(area)
