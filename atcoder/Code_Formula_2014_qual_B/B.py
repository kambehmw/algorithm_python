N = input()[::-1]
even = 0
odd = 0
for i, c in enumerate(N, 1):
    if i % 2 == 0:
        even += int(c)
    else:
        odd += int(c)
print(even, odd)