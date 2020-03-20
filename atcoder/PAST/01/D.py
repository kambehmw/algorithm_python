from collections import defaultdict
N = int(input())
A = [int(input()) for _ in range(N)]
counter = defaultdict(int)
for i in range(1, N+1):
    counter[i] = 0
for a in A:
    counter[a] += 1
x, y = None, None
for k, v in counter.items():
    if v == 0:
        x = k
    elif v == 2:
        y = k
if x is not None and y is not None:
    print(y, x)
else:
    print("Correct")