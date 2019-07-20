def total_price(x, y, N):
    if (x + y) == N:
        return True
    elif (x + y) > N:
        return False
    ret1 = total_price(x + 4, y, N)
    ret2 = total_price(x, y + 7, N)
    return ret1 or ret2

N = int(input())
if total_price(0, 0, N):
    print("Yes")
else:
    print("No")
