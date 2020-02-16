from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
counter = Counter(S)
max_val = max(counter.values())
for k, v in sorted(counter.items()):
    if v == max_val:
        print(k)