mod = 10 ** 9 + 7

N = int(input())
S1 = input()
S2 = input()
cnt = 0
if S1[0] == S2[0]:
    cnt += 3
    i = 1
    x = True
else:
    cnt += 6
    i = 2
    x = False

while i < N:
    if S1[i] == S2[i]:
        if x:
            cnt *= 2
        else:
            pass
        x = True
        i += 1
    else:
        if x:
            cnt *= 2
        else:
            cnt *= 3
        x = False
        i += 2
print(cnt % mod)
