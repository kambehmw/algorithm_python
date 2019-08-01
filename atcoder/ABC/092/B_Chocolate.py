N = int(input())
D, X = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))
count = 0
for a in A:
    i = 0
    while True:
        tmp = 1 + i * a
        if tmp <= D:
            count += 1
            i += 1
        else:
            break
print(count+X)