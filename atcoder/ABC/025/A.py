S = input()
N = int(input())
strs = []
for c1 in S:
    for c2 in S:
        strs.append(c1 + c2)
print(strs[N-1])