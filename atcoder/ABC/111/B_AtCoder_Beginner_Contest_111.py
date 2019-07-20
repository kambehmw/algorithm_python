N = int(input())
X = [111, 222, 333, 444, 555, 666, 777, 888, 999]
X = [x for x in X if x >= N]
print(min(X))