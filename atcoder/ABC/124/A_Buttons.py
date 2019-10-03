A, B = tuple(map(int, input().split()))
ans = 0
for i in range(2):
    if A < B:
        ans += B
        B -= 1
    else:
        ans += A
        A -= 1
print(ans)