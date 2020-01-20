N = int(input())
i = 0
result = []
while True:
    i += 1
    s = set(str(i))
    if len(s) == 1:
        result.append(i)
    if len(result) == N:
        break
print(result[N-1])
