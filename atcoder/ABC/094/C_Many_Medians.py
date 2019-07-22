N = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(X)
sorted_indices = sorted(range(len(X)), key=lambda k: X[k])
median_index = N // 2 - 1
ans = []
for i, x in enumerate(sorted_X):
    if i <= median_index:
        ans.append((sorted_indices[i], sorted_X[median_index + 1]))
    elif median_index < i:
        ans.append((sorted_indices[i], sorted_X[median_index]))
ans = sorted(ans, key=lambda x: x[0])
for x in ans:
    print(x[1])
