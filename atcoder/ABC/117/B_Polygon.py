N = int(input())
L = list(map(int, input().split()))
max_num = max(L)
total_sum = sum(L)
if (total_sum - max_num) > max_num:
    print("Yes")
else:
    print("No")