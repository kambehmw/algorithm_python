from collections import Counter
S = input()
counter = Counter(S)
for v in counter.values():
    if v != 1:
        print("no")
        exit()
print("yes")