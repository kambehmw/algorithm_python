A = int(input())
B = int(input())
C = int(input())
scores = [A, B, C]
ans = [None] * 3
for i in range(3):
    max_val = max(scores)
    ans[scores.index(max_val)] = i + 1
    scores[scores.index(max_val)] = 0
for x in ans:
    print(x)
