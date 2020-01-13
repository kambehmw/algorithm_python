n, X = tuple(map(int, input().split()))
A = list(map(int, input().split()))
total = 0
for i, b in enumerate(bin(X)[2:][::-1]):
    if b == "1":
        total += A[i]
print(total)