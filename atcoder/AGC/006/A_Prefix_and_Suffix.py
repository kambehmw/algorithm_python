N = int(input())
s = input()
t = input()

if s == t:
    print(N)
    exit()

res = 0
for i in range(N):
    if s[i:] == t[:N-i]:
        res = i
        break

if res == 0:
    print(len(s + t))
else:
    ans = s[:res] + t
    print(len(ans))