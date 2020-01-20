S = input()
X = list(map(int, input().split()))
ans = ""
for i, c in enumerate(S):
    if i in X:
        ans += '"' + c
    else:
        ans += c
if len(S) in X:
    ans += '"'
print(ans)
