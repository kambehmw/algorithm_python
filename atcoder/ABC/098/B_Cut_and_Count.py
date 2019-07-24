N = int(input())
S = input()
if N == 2:
    print(len(set(S[0]).intersection(set(S[1]))))
else:
    ans = []
    for i in range(1, N-1):
        a = set(S[:i])
        b = set(S[i:])
        ans.append(len(a.intersection(b)))
    print(max(ans))
