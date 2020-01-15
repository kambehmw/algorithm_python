N = int(input())
S = input()
res = "b"
if res == S:
    print(0)
    exit()

i = 1
while len(res) <= N:
    if i % 3 == 0:
        res = "b" + res + "b"
    elif i % 3 == 1:
        res = "a" + res + "c"
    elif i % 3 == 2:
        res = "c" + res + "a"

    if res == S:
        print(i)
        exit()

    i += 1
print(-1)
