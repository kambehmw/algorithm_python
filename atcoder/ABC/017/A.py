score = 0
for _ in range(3):
    s, e = tuple(map(int, input().split()))
    score += s * e // 10
print(score)
