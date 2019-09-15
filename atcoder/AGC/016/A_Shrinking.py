import copy
s = input()
N = len(s)
chr_set = set([c for c in s])
if len(chr_set) == 1:
    print(0)
    exit()

ans = []
for c in chr_set:
    count = 0
    t = copy.deepcopy(s)
    loop_len = N
    while True:
        tmp_t = ""
        for i in range(loop_len-1):
            if t[i] == c:
                tmp_t += c
            elif t[i+1] == c:
                tmp_t += c
            else:
                tmp_t += t[i]
        count += 1
        if len(set(tmp_t)) == 1:
            ans.append(count)
            break
        t = tmp_t
        loop_len -= 1

print(min(ans))