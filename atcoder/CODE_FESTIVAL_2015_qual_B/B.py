from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
counter = Counter(A)
ans = max(counter.items(), key=lambda x: x[1])
if N // 2 < ans[1]:
    print(ans[0])
else:
    print("?")