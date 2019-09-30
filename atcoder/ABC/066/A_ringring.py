a, b, c = tuple(map(int, input().split()))
print(min(a + b, b + c, c + a))