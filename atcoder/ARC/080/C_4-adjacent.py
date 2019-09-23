N = int(input())
A = list(map(int, input().split()))
div_4 = 0
div_2 = 0
div_0 = 0
for a in A:
    tmp = a
    count = 0
    while True:
        if tmp % 2 == 0:
            tmp = tmp // 2
            count += 1
        else:
            break
    if count == 0:
        div_0 += 1
    elif count == 1:
        div_2 += 1
    else:
        div_4 += 1
if div_2 == 0:
    if div_0 <= (div_4 + 1):
        print("Yes")
    else:
        print("No")
else:
    if div_0 <= div_4:
        print("Yes")
    else:
        print("No")
