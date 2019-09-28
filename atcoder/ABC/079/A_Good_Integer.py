N = input()
count = 0
for i in range(len(N)-1):
    if N[i] == N[i+1]:
        count += 1
    else:
        count = 0

    if count >= 2:
        print("Yes")
        exit()
print("No")
