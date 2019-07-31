N = int(input())
P = list(map(int, input().split()))
sorted_P = sorted(P)
count = 0
for i, p in enumerate(P):
    if p != sorted_P[i]:
        count += 1
if count == 0 or count == 2:
    print("YES")
else:
    print("NO")
