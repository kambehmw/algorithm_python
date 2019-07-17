N = int(input())
S = []
for i in range(N):
    S.append(input())

names = {}
for s in S:
    initial = s[0]
    if initial not in names:
        names[initial] = 0
    names[initial] += 1

initial_keys = set(names.keys()).intersection({"M", "A", "R", "C", "H"})
if len(initial_keys) < 3:
    print(0)
else:
    initials = ["M", "A", "R", "C", "H"]
    count = 0
    for i in range(len(initials)-2):
        for j in range(i+1, len(initials)-1):
            for k in range(j+1, len(initials)):
                count += (names.get(initials[i], 0) * names.get(initials[j], 0) * names.get(initials[k], 0))
    print(count)
