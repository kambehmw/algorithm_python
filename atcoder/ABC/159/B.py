S = input()
N = len(S)
if S == S[::-1]:
    tmp = S[:(N - 1) // 2]
    if tmp == tmp[::-1]:
        t = S[(N + 3) // 2 - 1:N]
        if t == t[::-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")