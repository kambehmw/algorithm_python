S = input()
for i, s in enumerate(S):
    if i % 2 == 0:
        if s == "L":
            print("No")
            exit()
    else:
        if s == "R":
            print("No")
            exit()
print("Yes")