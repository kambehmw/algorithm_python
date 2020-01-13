L, H = tuple(map(int, input().split()))
N = int(input())
A = [int(input()) for _ in range(N)]
total = 0
for a in A:
    if a < L:
        print(L - a)
    elif a <= H:
        print(0)
    else:
        print(-1)
