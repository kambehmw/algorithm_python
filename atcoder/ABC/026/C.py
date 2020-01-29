def dfs(n):
    if len(sub[n]) == 0:
        return 1
    min_val, max_val = float('inf'), float('-inf')
    for i in sub[n]:
        p = dfs(i)
        min_val = min(min_val, p)
        max_val = max(max_val, p)
    return max_val + min_val + 1


N = int(input())
B = []
for _ in range(N-1):
    b = int(input())
    B.append(b)
sub = [[] for _ in range(N+1)]
for i, b in enumerate(B, 2):
    sub[b].append(i)
print(dfs(1))
