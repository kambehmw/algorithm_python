N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
d_dict = {}
for d in D:
    if d not in d_dict:
        d_dict[d] = 0
    d_dict[d] += 1

count = 0
for t in T:
    if t in d_dict and d_dict[t] > 0:
        d_dict[t] -= 1
        count += 1
if count == M:
    print("YES")
else:
    print("NO")