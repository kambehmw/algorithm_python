N = int(input())
A = list(map(int, input().split()))
ok, bad = 1, 1
for a in A:
    ok *= 3
    if a % 2 == 0:
        bad *= 2
print(ok - bad)
