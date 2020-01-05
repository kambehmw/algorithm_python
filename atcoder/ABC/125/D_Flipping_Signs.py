N = int(input())
A = list(map(int, input().split()))
num_negative = 0
zero_flag = False
for a in A:
    if zero_flag:
        zero_flag = True
    if a < 0:
        num_negative += 1
total = sum([abs(a) for a in A])
if num_negative % 2 == 0 or zero_flag:
    print(total)
else:
    print(total - 2 * min([abs(a) for a in A]))