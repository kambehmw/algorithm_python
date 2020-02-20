C = int(input())
A = [list(map(int, input().split())) for _ in range(C)]
sorted_A = [sorted(a) for a in A]
ans = 1
for i in range(3):
    max_val = 0
    for a in sorted_A:
        max_val = max(max_val, a[i])
    ans *= max_val
print(ans)