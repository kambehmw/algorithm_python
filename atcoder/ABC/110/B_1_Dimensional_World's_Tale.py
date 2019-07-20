N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

for i in range(X+1, Y+1):
    flag1 = all([True if x < i else False for x in xs])
    flag2 = all(True if y >= i else False for y in ys)
    if flag1 and flag2:
        print("No War")
        exit()
print("War")