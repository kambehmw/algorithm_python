N = int(input())
T, A = [], []
for _ in range(N):
    t, a = tuple(map(int, input().split()))
    T.append(t)
    A.append(a)
x, y = 1, 1
for t, a in zip(T, A):
    n = max(-(-x // t), -(-y // a))
    x = n * t
    y = n * a
print(x + y)