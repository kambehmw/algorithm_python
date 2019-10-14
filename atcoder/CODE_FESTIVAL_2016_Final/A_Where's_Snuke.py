H, W = tuple(map(int, input().split()))
for h in range(H):
    row = input().split()
    for i, s in enumerate(row):
        if s == "snuke":
            print(chr(ord("A") + i) + str(h+1))
            exit()