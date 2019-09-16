from collections import Counter

n = int(input())
A = Counter(list(map(int, input().split())))
x = [0, 0]
for a in A:
    if A[a] >= 2:
        x.append(a)
    if A[a] >= 4:
        x.append(a)
x.sort()
print(x[-1] * x[-2])
