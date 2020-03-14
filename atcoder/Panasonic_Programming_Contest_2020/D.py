import string
ans = []
N = int(input())

def rec(s, i):
    if len(s) == N:
        ans.append(s)
        return

    for c in string.ascii_lowercase[:i + 1]:
        if c == string.ascii_lowercase[i]:
            rec(s + c, i + 1)
        else:
            rec(s + c, i)

rec("a", 1)
for x in ans:
    print(x)