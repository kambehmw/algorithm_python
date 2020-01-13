from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
counter = Counter(S)
print(sorted(counter.items(), key=lambda x: x[1])[-1][0])
