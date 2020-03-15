N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()
print(sum(d))
if 1 < N and sum(d[:-1]) > d[-1]:
    print(0)
else:
    print(d[-1] - sum(d[:-1]))