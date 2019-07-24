N = int(input())
H = list(map(int, input().split()))
count = 0
while sum(H) != 0:
    for i in range(N):
        if i == N - 1:
            if H[i] != 0:
                count += 1
        else:
            if H[i] != 0 and H[i+1] == 0:
                count += 1
        if H[i] > 0:
            H[i] -= 1
print(count)