N = int(input())
for i in range(2, N):
    if N % i == 0:
        print("NO")
        exit()
print("YES")