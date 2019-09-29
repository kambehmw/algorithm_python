N = int(input())
A = list(map(int, input().split()))
counts = [0] * (N + 1)
ball_counts = 0
balls = []
for i in range(N-1, -1, -1):
    if sum(counts[::i+1][1:]) % 2 != A[i]:
        ball_counts += 1
        balls.append(i+1)
        counts[i+1] = 1
print(ball_counts)
if ball_counts > 0:
    print(*balls)
