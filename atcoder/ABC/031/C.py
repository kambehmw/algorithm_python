N = int(input())
A = list(map(int, input().split()))
ans = float('-inf')
for i in range(N):
    max_score = float('-inf')
    max_start, max_end = None, None
    for j in range(N):
        if i == j:
            continue
        if i < j:
            start, end = i, j
        else:
            start, end = j, i
        score = sum(A[start:end+1][1::2])
        if max_score < score:
            max_score = score
            max_start, max_end = start, end
    ans = max(ans, sum(A[max_start:max_end+1][::2]))
print(ans)
