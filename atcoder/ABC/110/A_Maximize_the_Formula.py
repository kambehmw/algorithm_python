A, B, C = tuple(map(int, input().split()))
l = [A, B, C]
l.sort()
print(l[-1] * 10 + l[0] + l[1])