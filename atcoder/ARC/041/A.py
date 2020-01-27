x, y = map(int, input().split())
k = int(input())
if y < k:
    print(x + y - (k - y))
else:
    print(x + k)