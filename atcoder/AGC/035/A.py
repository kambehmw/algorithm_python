N = int(input())
A = list(map(int, input().split()))

res = A[0] ^ A[1]
for i in range(2, N):
    res ^= A[i]
if res == 0:
    print("Yes")
else:
    print("No")