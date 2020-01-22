from collections import Counter
N = int(input())
R = input()
counter = Counter(R)
eval = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
score = sum([eval[k] * v for k, v in counter.items()])
score /= N
print(score)