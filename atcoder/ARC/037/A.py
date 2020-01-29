N = int(input())
M = list(map(int, input().split()))
total = 0
for m in M:
    if m < 80:
        total += (80 - m)
print(total)