W, H, N = list(map(int, input().split()))
x_min, x_max = 0, W
y_min, y_max = 0, H
for i in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        if x_min < x:
            x_min = x
    elif a == 2:
        if x < x_max:
            x_max = x
    elif a == 3:
        if y_min < y:
            y_min = y
    elif a == 4:
        if y < y_max:
            y_max = y
if x_max < x_min:
    print(0)
elif y_max < y_min:
    print(0)
else:
    print((x_max - x_min) * (y_max - y_min))