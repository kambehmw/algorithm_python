x = int(input())
div = x // 11
mod = x % 11
if mod == 0:
    print(div * 2)
elif mod <= 6:
    print(div * 2 + 1)
else:
    print(div * 2 + 2)