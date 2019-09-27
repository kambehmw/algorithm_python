X, A, B = tuple(map(int, input().split()))
if (B - A) > X:
    print("dangerous")
else:
    if A >= B:
        print("delicious")
    else:
        print("safe")