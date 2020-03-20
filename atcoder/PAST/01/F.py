S = input()
now = False
word = ""
ans = []
for c in S:
    word += c
    if c.isupper():
        now = not now
        if not now:
            ans.append(word)
            word = ""

ans.sort(key=lambda x: x.lower())
# print(ans)
print("".join(ans))