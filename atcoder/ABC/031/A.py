A, D = tuple(map(int, input().split()))
if (A + 1) * D < A * (D + 1):
    D += 1
elif (A + 1) * D > A * (D + 1):
    A += 1
else:
    A += 1
print(A * D)
