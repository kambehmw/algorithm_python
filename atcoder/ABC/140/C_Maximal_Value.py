N = int(input())
B = list(map(int, input().split()))
A = [0] * N
for i in range(N):
    first = B[i] if 0 <= i < len(B) else float('inf')
    second = B[i-1] if 0 <= i-1 < len(B) else float('inf')
    A[i] = min(first, second)
print(sum(A))