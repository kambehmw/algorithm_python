N = int(input())
A, B = [], []
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)
count = 0
for i in range(N-1, -1, -1):
    if (A[i] + count) % B[i] == 0:
        continue
    count += (B[i] - ((A[i] + count) % B[i]))
print(count)