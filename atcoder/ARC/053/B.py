from collections import Counter
S = input()
counter = Counter(S)
odds, evens = 0, 0
for k, v in counter.items():
    if v % 2 == 0:
        evens += v
    else:
        odds += 1
        evens += (v - 1)

if odds == 0:
    print(evens)
    exit()

res = [1] * odds
i = 0
while 0 < evens:
    res[i] += 2
    evens -= 2
    i += 1
    if len(res) <= i:
        i = 0
print(min(res))

