T = int(input())
S = [input() for _ in range(T)]
for s in S:
    st = set(s)
    if len(st) == 1:
        print(s)
    else:
        ans = ""
        for i in range(len(s) - 1):
            ans += s[i]
            if s[i] == s[i + 1]:
                if s[i] == "1":
                    ans += "0"
                else:
                    ans += "1"
        ans += s[-1]
        print(ans)