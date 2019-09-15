import string
S = set([c for c in input()])
for c in string.ascii_lowercase:
    if c not in S:
        print(c)
        exit()
print("None")