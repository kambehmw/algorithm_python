s = int(input())
integers = {s}
count = 1
while True:
    count += 1
    if s % 2 == 0:
        tmp = s / 2
    else:
        tmp = 3 * s + 1
    if tmp in integers:
        break
    integers.add(tmp)
    s = tmp
print(count)