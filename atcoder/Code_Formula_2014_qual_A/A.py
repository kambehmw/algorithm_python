A = int(input())
for i in range(1, 10 ** 6 + 1):
    if i ** 3 == A:
        print("YES")
        exit()
print("NO")