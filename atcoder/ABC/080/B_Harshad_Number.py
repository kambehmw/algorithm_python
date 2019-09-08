import copy

N = int(input())
X = copy.deepcopy(N)
fx = 0
while X > 0:
    fx += X % 10
    X = X // 10
if N % fx == 0:
    print("Yes")
else:
    print("No")