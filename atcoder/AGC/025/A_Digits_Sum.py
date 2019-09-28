N = int(input())
ans = float('inf')
for i in range(1, N):
    A = i
    B = N - i
    total = sum([int(c) for c in str(A)])
    total += sum([int(c) for c in str(B)])
    ans = min(ans, total)
print(ans)