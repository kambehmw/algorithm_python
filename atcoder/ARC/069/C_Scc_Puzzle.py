N, M = list(map(int, input().split()))
count = 0
if N >= (M // 2):
    count += (M // 2)
else:
    count += N
    M -= (2 * N)
    count += (M // 4)
print(count)
