N = int(input())
s = input()
animals = ["S", "W"]
for s1 in animals:
    for s2 in animals:
        t = [s1, s2]
        for i in range(1, N-1):
            if s[i] == "o":
                if t[i] == "S":
                    if t[i-1] == "S":
                        t.append("S")
                    else:
                        t.append("W")
                else:
                    if t[i-1] == "S":
                        t.append("W")
                    else:
                        t.append("S")
            else:
                if t[i] == "S":
                    if t[i-1] == "S":
                        t.append("W")
                    else:
                        t.append("S")
                else:
                    if t[i-1] == "S":
                        t.append("S")
                    else:
                        t.append("W")
        ans = ""
        for i in range(N):
            prev = i - 1 if 0 <= i - 1 else N - 1
            next = i + 1 if i + 1 < N else 0
            if t[i] == "S":
                if t[prev] == t[next]:
                    ans += "o"
                else:
                    ans += "x"
            else:
                if t[prev] == t[next]:
                    ans += "x"
                else:
                    ans += "o"
        if ans == s:
            print("".join(t))
            exit()
print(-1)
