N = int(input())
ans = float('inf')
for A in range(1, int(N**0.5)+1):
    if N % A == 0:
        B = N // A
        ans = min(ans, max(len(str(A)), len(str(B))))
print(ans)