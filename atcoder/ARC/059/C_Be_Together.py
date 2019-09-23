N = int(input())
A = list(map(int, input().split()))
ans = float('inf')
for i in range(-100, 101):
    ans = min(ans, sum([abs(a - i) ** 2 for a in A]))
print(ans)