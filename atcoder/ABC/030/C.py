N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i, j = 0, 0
time, cnt = 0, 0
loc = True
while True:
    if i == N and loc or j == M and not loc:
        break

    if loc:
        if time <= A[i]:
            time = A[i] + X
            loc = not loc
        i += 1
    else:
        if time <= B[j]:
            time = B[j] + Y
            loc = not loc
            cnt += 1
        j += 1
print(cnt)