from collections import defaultdict
S = input()
T = input()
d = defaultdict(set)
for s, t in zip(S, T):
    d[s].add(t)

for v in d.values():
    if len(v) != 1:
        print("No")
        exit()

chars = set()
for k, v in d.items():
    for x in v:
        if x in chars:
            print("No")
            exit()
        chars.add(x)
print("Yes")