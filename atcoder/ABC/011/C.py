N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
if N == NG1 or N == NG2 or N == NG3:
    print("NO")
    exit()

cnt = 0
while 0 < N:
    tmp = N - 3
    if tmp == NG1 or tmp == NG2 or tmp == NG3:
        tmp = N - 2
        if tmp == NG1 or tmp == NG2 or tmp == NG3:
            tmp = N - 1
            if tmp == NG1 or tmp == NG2 or tmp == NG3:
                print("NO")
                exit()

    cnt += 1
    N = tmp

if cnt > 100:
    print("NO")
else:
    print("YES")