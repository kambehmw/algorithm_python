A, B, C = list(map(int, input().split()))
K = int(input())
for i in range(K):
    max_val = max(A, B, C)
    if max_val == A:
        A *= 2
    elif max_val == B:
        B *= 2
    elif max_val == C:
        C *= 2
print(sum([A, B, C]))