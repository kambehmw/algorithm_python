import math
import itertools
N = int(input())
pos = []
for _ in range(N):
    tmp = tuple(map(int, input().split()))
    pos.append(tmp)

ave = 0
cnt = 0
for x in itertools.permutations(pos):
    for i in range(N-1):
        ave += math.sqrt((x[i][0] - x[i+1][0]) ** 2 + (x[i][1] - x[i+1][1]) ** 2)
    cnt += 1
print(ave / cnt)
