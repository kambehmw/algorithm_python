X, Y = tuple(map(int, input().split()))
count = 1
tmp = X
while True:
    tmp *= 2
    if tmp > Y:
        break
    count += 1
print(count)