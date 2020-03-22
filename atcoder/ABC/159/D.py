from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = 0
for k, v in counter.items():
    if 2 <= v:
        ans += v * (v - 1) // 2
for a in A:
    if a in counter and 2 <= counter[a]:
        v = counter[a]
        diff = v * (v - 1) // 2 - ((v- 1) * (v - 2) // 2)
        print(ans - diff)
    else:
        print(ans)