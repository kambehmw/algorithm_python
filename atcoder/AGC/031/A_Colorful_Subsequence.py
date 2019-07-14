N = int(input())
S = input()

char2count = {}
for s in S:
    if s not in char2count:
        char2count[s] = 0
    char2count[s] += 1

total = 1
for x in char2count.values():
    total *= (x + 1)
print((total - 1) % (1000000000 + 7))
