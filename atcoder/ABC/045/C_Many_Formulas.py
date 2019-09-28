S = input()
N = len(S) - 1
ans = 0
for i in range(2**N):
    t = S[0]
    for j in range(N):
        if (i >> j) & 1 == 1:
            t += "+"
        t += S[j+1]
    ans += eval(t)
print(ans)