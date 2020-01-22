N = int(input())
N %= 30
result = [1, 2, 3, 4, 5, 6]
for i in range(N):
    i %= 5
    result[i], result[i+1] = result[i+1], result[i]
print("".join(map(str, result)))