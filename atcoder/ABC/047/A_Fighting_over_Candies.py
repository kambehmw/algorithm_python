a, b, c = tuple(map(int, input().split()))
if (a + b) == c:
    print("Yes")
elif (b + c) == a:
    print("Yes")
elif (c + a) == b:
    print("Yes")
else:
    print("No")