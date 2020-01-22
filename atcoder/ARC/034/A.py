N = int(input())
scores = []
for _ in range(N):
    score = list(map(int, input().split()))
    scores.append(score)
max_val = 0
for score in scores:
    total = sum(score[:4]) + 110 / 900 * score[4]
    max_val = max(max_val, total)
print(max_val)