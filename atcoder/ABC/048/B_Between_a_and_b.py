a, b, x = list(map(int, input().split()))
count = b // x
count -= (a - 1) //x
print(count)