xa, ya, xb, yb, xc, yc = tuple(map(int, input().split()))
xb -= xa
yb -= ya
xc -= xa
yc -= ya
xa, ya = 0, 0
print(abs(xb * yc - yb * xc) / 2)
