n = int(input())
x = [1, 1]
for i in range(2, n+1):
    x.append(x[i-2] + x[i-1])
print(x[n])