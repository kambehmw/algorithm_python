n, m = tuple(map(int, input().split()))
minutes = n * 60 + m
n_angle = 0.5 * minutes % 360
m_angle = 6 * minutes % 360
angle_diff = abs(n_angle - m_angle)
print(min(angle_diff, 360 - angle_diff))