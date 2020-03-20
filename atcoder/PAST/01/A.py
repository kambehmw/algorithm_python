S = input()
for c in S:
    if not c.isdigit():
        print("error")
        exit()
print(int(S) * 2)