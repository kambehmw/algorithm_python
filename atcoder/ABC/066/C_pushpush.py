from collections import deque
n = int(input())
A = list(map(int, input().split()))
even_odd = n % 2
b = deque()
for i, a in enumerate(A, 1):
    if i % 2 == even_odd:
        b.appendleft(a)
    else:
        b.append(a)
print(*b)