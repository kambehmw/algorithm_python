from collections import Counter
N = int(input())
a, b = tuple(map(int, input().split()))
K = int(input())
P = list(map(int, input().split()))
counter = Counter(P)
if a in counter or b in counter:
    print("NO")
    exit()

for k, v in counter.items():
    if v != 1:
        print("NO")
        exit()
print("YES")