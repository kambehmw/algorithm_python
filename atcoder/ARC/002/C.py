import itertools
N = int(input())
C = input()
C += "D" # dummy variable
command = ["A", "B", "X", "Y"]
ans = float('inf')
for L in itertools.product(command, repeat=2):
    L = "".join(L)
    for R in itertools.product(command, repeat=2):
        R = "".join(R)
        # print(L, R)
        if L == R:
            continue

        cnt = 0
        i = 0
        while i < N:
            tmp = C[i] + C[i+1]
            if tmp == L or tmp == R:
                i += 2
            else:
                i += 1
            cnt += 1
        ans = min(ans, cnt)
print(ans)