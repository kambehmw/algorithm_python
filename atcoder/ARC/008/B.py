from collections import Counter
import math
N, M = map(int, input().split())
name = input()
kit = input()
s_name = set(name)
s_kit = set(kit)
for s in s_name:
    if s not in s_kit:
        print(-1)
        exit()
ans = 0
name_cnt = Counter(name)
kit_cnt = Counter(kit)
for k, v in name_cnt.items():
    tmp = math.ceil(v / kit_cnt[k])
    ans = max(ans, tmp)
print(ans)