N = int(input())
L = list(map(int, input().split()))
L.sort()
result = 0
for x in range(N):
    z = x + 2
    for y in range(x+1, N):
        while z < N and L[x] + L[y] > L[z]:
            z += 1
        result += z - y - 1
print(result)