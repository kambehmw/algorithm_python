N = int(input())
B = list(map(int, input().split()))
res = []
while 0 < len(B):
    index = None
    for i, b in enumerate(B, 1):
        if i == b:
            index = i
    if index is None:
        print(-1)
        exit()
    else:
        res.append(B[index-1])
    del B[index-1]
for x in res[::-1]:
    print(x)