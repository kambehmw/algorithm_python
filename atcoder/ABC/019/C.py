N = int(input())
A = list(map(int, input().split()))
A.sort()
used = {}
for a in A:
    tmp = a
    while 0 < a and a % 2 == 0:
        a = a // 2
        if a in used:
            break
    if a not in used:
        used[tmp] = True

ans = len(used.keys())
print(ans)