import copy
N, Q = map(int, input().split())
follow = [["N" for _ in range(N)] for _ in range(N)]
for _ in range(Q):
    S = list(map(int, input().split()))
    s1 = S[0]
    if s1 == 1:
        s2 = S[1] - 1
        s3 = S[2] - 1
        follow[s2][s3] = "Y"
    elif s1 == 2:
        s2 = S[1] - 1
        for h in range(N):
            if h == s2:
                continue
            if follow[h][s2] == "Y":
                follow[s2][h] = "Y"
    elif s1 == 3:
        a = S[1] - 1
        row = copy.deepcopy(follow[a])
        for w in range(N):
            if row[w] == "Y":
                for w2 in range(N):
                    # print(w, w2)
                    if w2 == a:
                        continue
                    if follow[w][w2] == "Y":
                        follow[a][w2] = "Y"

for x in follow:
    print("".join(x))
