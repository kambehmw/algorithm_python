N = int(input())
S = []
for i in range(N):
    S.append(input())
M = int(input())
T = []
for i in range(M):
    T.append(input())

str2count1 = {}
for s in S:
    if s not in str2count1:
        str2count1[s] = 0
    str2count1[s] += 1

str2count2 = {}
for t in T:
    if t not in str2count2:
        str2count2[t] = 0
    str2count2[t] += 1

max_diff = 0
for key, value in str2count1.items():
    diff = value - str2count2[key] if key in str2count2 else value
    if max_diff < diff:
        max_diff = diff
print(max_diff)