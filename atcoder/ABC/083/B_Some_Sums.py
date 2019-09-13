import copy
N, A, B = list(map(int, input().split()))
total = 0
for i in range(1, N+1):
    tmp_i = copy.deepcopy(i)
    digits_sum = 0
    while tmp_i > 0:
        digits_sum += tmp_i % 10
        tmp_i = tmp_i // 10
    if A <= digits_sum <= B:
        total += i
print(total)