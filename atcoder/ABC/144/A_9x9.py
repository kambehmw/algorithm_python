A, B = tuple(map(int, input().split()))
if 10 <= A or 10 <= B:
    print(-1)
else:
    print(A * B)