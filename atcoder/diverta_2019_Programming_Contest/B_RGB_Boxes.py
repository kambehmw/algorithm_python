R, G, B, N = tuple(map(int, input().split()))
ans = 0
for i in range(N//R+1):
    for j in range(N//G+1):
        rest = (N - R * i - G * j)
        if rest < 0:
            break
        if rest % B == 0:
            ans += 1
print(ans)