N, x = tuple(map(int, input().split()))
A = list(map(int, input().split()))
A = sorted(A)
count = 0
for a in A[:-1]:
    if a <= x:
        count += 1
        x -= a

if A[-1] == x:
    count += 1
print(count)
