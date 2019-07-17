N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_diff = float('inf')
min_index = None
for i, h in enumerate(H):
    ave_temp = T - h * 0.006
    diff = abs(ave_temp - A)
    if diff < min_diff:
        min_diff = diff
        min_index = i
print(min_index + 1)
