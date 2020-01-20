from collections import Counter
L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
cnt = 0
counter_l = Counter(l)
counter_r = Counter(r)
for k, v in counter_l.items():
    if k in counter_r:
        while 0 < counter_l[k] and 0 < counter_r[k]:
            cnt += 1
            counter_r[k] -= 1
            counter_l[k] -= 1
print(cnt)