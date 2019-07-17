N, M = map(int, input().split())
X = list(map(int, input().split()))

X = sorted(X)
diff_dict = {}
for i in range(M-1):
    diff = X[i+1] - X[i]
    diff_dict[i] = diff
sorted_diff = sorted(diff_dict.items(), key=lambda x: x[1])[::-1][:N-1]
keys = {x[0] for x in sorted_diff}
tmp = []
count = 0
for i, x in enumerate(X):
    tmp.append(x)
    if i in keys:
        if len(tmp) > 1:
            count += (max(tmp) - min(tmp))
        tmp.clear()
if len(tmp) > 1:
    count += (max(tmp) - min(tmp))
print(count)
