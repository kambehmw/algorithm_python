N = int(input())
S = [int(input()) for _ in range(N)]
S = sorted(S)
grade = sum(S)
if grade % 10 != 0:
    print(grade)
    exit()
for s in S:
    tmp = grade - s
    if tmp % 10 != 0:
        print(tmp)
        exit()
print(0)