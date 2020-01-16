N = int(input())
W = input()[:-1].split(" ")
cnt = 0
words = {"TAKAHASHIKUN", "Takahashikun", "takahashikun"}
for w in W:
    if w in words:
        cnt += 1
print(cnt)