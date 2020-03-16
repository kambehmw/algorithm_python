from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
T = "indeednow"
counter = Counter(T)
for s in S:
    if len(s) != len(T):
        print("NO")
        continue

    counter2 = Counter(s)
    flag = True
    for k, v in counter2.items():
        if k not in counter:
            flag = False
            break

        if counter[k] != v:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")