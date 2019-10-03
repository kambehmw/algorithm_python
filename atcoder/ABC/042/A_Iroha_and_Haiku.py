from collections import Counter
A, B, C = tuple(map(int, input().split()))
counter = Counter([A, B, C])
if counter[5] == 2 and counter[7] == 1:
    print("YES")
else:
    print("NO")