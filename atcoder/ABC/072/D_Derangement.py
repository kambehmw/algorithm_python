N = int(input())
P = list(map(int, input().split()))
count = 0
for i in range(N-1):
    if i + 1 == P[i]:
        P[i], P[i+1] = P[i+1], P[i]
        count += 1

if N == P[N-1]:
    count += 1
print(count)