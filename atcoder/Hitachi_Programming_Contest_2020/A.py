S = input()
tmp = ""
for i in range(5):
    tmp += "hi"
    if tmp == S:
        print("Yes")
        exit()
print("No")