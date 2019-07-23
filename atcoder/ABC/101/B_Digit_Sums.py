N = input()
total_sum = 0
for s in N:
    total_sum += int(s)
if int(N) % total_sum == 0:
    print("Yes")
else:
    print("No")