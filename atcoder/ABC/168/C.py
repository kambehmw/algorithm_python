import math
A, B, H, M = map(int, input().split())
angle1 = (H + M / 60) * 30
angle2 = M * 6
angle = abs(angle1 - angle2)
if angle > 180:
    angle = 360 - angle
ans = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle))
print(math.sqrt(ans))