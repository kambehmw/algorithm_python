a, b = map(int, input().split())
X = [1]
for i in range(1, 999):
    X.append(X[i-1]+i+1)
diff = b - a
print(X[diff-1] - b)