N = int(input())
A = [int(input()) for i in range(N)]
sorted_A = sorted(A)
max_num = sorted_A[-1]
for a in A:
    if a == max_num:
        print(sorted_A[-2])
    else:
        print(max_num)