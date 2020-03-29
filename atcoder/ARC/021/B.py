L = int(input())
B = [int(input()) for _ in range(L)]
xor = B[0]
for i in range(1, L-1):
    xor ^= B[i]
A = [0]
if xor == B[-1]:
    for i in range(L-1):
        A.append(A[-1] ^ B[i])
    for a in A:
        print(a)
else:
    print(-1)