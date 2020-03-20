from collections import Counter
N = int(input())
S = input()
counter = Counter(S)
ans = 0
for k, v in counter.items():
    if v % 2 != 0:
        ans += v % 2
print(ans)
