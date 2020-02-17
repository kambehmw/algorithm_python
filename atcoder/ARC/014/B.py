N = int(input())
W = [input() for _ in range(N)]
words = set()
for i, w in enumerate(W):
    if w in words:
        if i % 2 == 0:
            print("LOSE")
        else:
            print("WIN")
        exit()
    else:
        words.add(w)

    if i >= 1:
        if W[i-1][-1] != W[i][0]:
            if i % 2 == 0:
                print("LOSE")
            else:
                print("WIN")
            exit()
print("DRAW")