from collections import Counter
S = input()
counter = Counter(S)
for c in ["a", "b", "c"]:
    if c not in counter:
        counter[c] = 0
if (max(counter.values()) - min(counter.values())) <= 1:
    print("YES")
else:
    print("NO")