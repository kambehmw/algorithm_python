S = input()
K = int(input())
if len(set(S)) == 1:
    print(len(S) * K // 2)
    exit()

i = 0
cnt = 0
while i + 1 < len(S):
    if S[i] == S[i + 1]:
        cnt += 1
        i += 2
    else:
        i += 1

if S[0] != S[-1]:
    print(cnt * K)
else:
    i = 1
    a = 1
    prev = S[0]
    while i < len(S):
        if prev != S[i]:
            break
        else:
            a += 1
        i += 1
    prev = S[-1]
    b = 1
    i = len(S) - 2
    while 0 <= i:
        if prev != S[i]:
            break
        else:
            b += 1
        i -= 1
    print(cnt * K - (K - 1) * (a // 2 + b // 2 - (a + b) // 2))