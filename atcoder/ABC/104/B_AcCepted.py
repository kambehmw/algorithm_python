S = input()
if S[0] != "A":
    print("WA")
    exit()

if S[2:-1].count("C") != 1:
    print("WA")
    exit()

C_index = None
for i, s in enumerate(S[2:-1], 2):
    if s == "C":
        C_index = i
        break

for i, s in enumerate(S[1:], 1):
    if i == C_index:
        continue

    if s.isupper():
        print("WA")
        exit()
print("AC")
