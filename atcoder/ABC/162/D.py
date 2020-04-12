N = int(input())
S = input()
r, g, b = 0, 0, 0
for c in S:
    if c == "R":
        r += 1
    elif c == "G":
        g += 1
    else:
        b += 1
ans = r * g * b
sub = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            continue
        k = 2 * j - i
        if k >= N or S[k] == S[i] or S[k] == S[j]:
            continue
        sub += 1
print(ans - sub)