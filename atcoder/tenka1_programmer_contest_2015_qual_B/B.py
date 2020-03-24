S = input()
if S == "{}":
    print("dict")
    exit()

cnt = 0
for c in S:
    if c == "{":
        cnt += 1
    elif c == "}":
        cnt -= 1

    if cnt == 1 and c == ":":
        print("dict")
        exit()
print("set")
