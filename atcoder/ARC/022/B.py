N = int(input())
A = list(map(int, input().split()))
s = [0] * (10 ** 5 + 1)
front, back = 0, 0
ans = 0
while front < N:
    s[A[front]] += 1
    # print(front, back)
    while s[A[front]] > 1:
        # print(back, front)
        ans = max(ans, front - back)
        s[A[back]] -= 1
        back += 1
    front += 1
ans = max(ans, front - back)
print(ans)