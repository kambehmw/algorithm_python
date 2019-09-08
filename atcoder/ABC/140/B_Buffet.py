N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
prev_eat = None
ans = 0
for i in range(N):
    dish_idx = A[i]
    ans += B[dish_idx-1]
    if prev_eat is not None and prev_eat + 1 == dish_idx:
        ans += C[prev_eat-1]
    prev_eat = dish_idx
print(ans)
