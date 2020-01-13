S = input()
T = input()
check_chars = {'a', 't', 'c', 'o', 'd', 'e', 'r'}
for s, t in zip(S, T):
    if s == t:
        continue
    if s == "@":
        if t not in check_chars:
            print("You will lose")
            exit()
    elif t == "@":
        if s not in check_chars:
            print("You will lose")
            exit()
    else:
        print("You will lose")
        exit()
print("You can win")