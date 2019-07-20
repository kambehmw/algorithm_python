N = int(input())
W = [input() for i in range(N)]

vocab = {W[0]}
for i in range(1, N):
    if W[i] in vocab:
        print("No")
        exit()
    vocab.add(W[i])

    if W[i-1][-1] != W[i][0]:
        print("No")
        exit()
print("Yes")