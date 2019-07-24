N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
counts = []
for i in range(N):
    total = sum(A[0][:i+1])
    total += sum(A[1][i:])
    counts.append(total)
print(max(counts))