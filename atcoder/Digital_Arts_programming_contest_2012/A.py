s = list(input().split())
N = int(input())
t = [input() for _ in range(N)]
ans = []
for w1 in s:
    flag2 = True
    for w2 in t:
        if len(w1) != len(w2):
            continue
        flag = True
        for c1, c2 in zip(w1, w2):
            if c2 == "*" or c1 == c2:
                continue
            else:
                flag = False
                break
        if flag:
            ans.append("*" * len(w1))
            flag2 = False
            break
    if flag2:
        ans.append(w1)

print(" ".join(ans))