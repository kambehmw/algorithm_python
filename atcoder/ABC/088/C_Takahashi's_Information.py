C = []
for i in range(3):
    C.append(list(map(int, input().split())))
A = [0]
B = [C[0][i] - A[0] for i in range(3)]
for i in range(1, 3):
    A.append(C[i][0] - B[0])
for i, a in enumerate(A):
    for j, b in enumerate(B):
        if a + b != C[i][j]:
            print("No")
            exit()
print("Yes")