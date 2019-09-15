from collections import Counter
w = input()
counter = Counter(w)
for v in counter.values():
    if v % 2 != 0:
        print("No")
        exit()
print("Yes")