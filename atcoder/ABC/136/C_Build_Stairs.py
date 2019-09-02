N = int(input())
H = list(map(int, input().split()))
reverse_H = H[::-1]
for i in range(N-1):
    if reverse_H[i] < reverse_H[i+1]:
        if reverse_H[i] < reverse_H[i+1] - 1:
            print("No")
            exit()
        reverse_H[i+1] -= 1
print("Yes")