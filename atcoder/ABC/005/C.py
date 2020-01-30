T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
if N < M:
    print("no")
    exit()
is_sold = [False] * N
for b in B:
    flag = False
    for i, a in enumerate(A):
        if is_sold[i]:
            continue
        if a <= b and abs(b - a) <= T:
            is_sold[i] = True
            flag = True
            break
    if not flag:
        print("no")
        exit()
print("yes")