N = int(input())
total = 0.0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b
print(int(total * 1.05))