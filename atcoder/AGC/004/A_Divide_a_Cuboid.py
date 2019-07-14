A, B, C = map(int, input().split())
max_num = max(A, B, C)
if max_num == A:
    res1 = (A // 2) * B * C
    res2 = (A - (A // 2)) * B * C
elif max_num == B:
    res1 = (B // 2) * A * C
    res2 = (B - (B // 2)) * A * C
elif max_num == C:
    res1 = (C // 2) * B * A
    res2 = (C - (C // 2)) * B * A
print(abs(res1 - res2))