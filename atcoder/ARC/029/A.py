N = int(input())
T = [int(input()) for _ in range(N)]
ans = float('inf')
total = sum(T)
for x in range(2**N):
    total1 = 0
    for i, b in enumerate(bin(x)[2:][::-1]):
        if b == "0":
            total1 += T[int(i)]
    ans = min(ans, max(total1, total - total1))
print(ans)