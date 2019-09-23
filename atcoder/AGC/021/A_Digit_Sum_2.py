N = input()
if len(N) == 1:
    print(int(N))
    exit()

for c in N[1:]:
    if c != "9":
        print(int(N[0]) - 1 + (len(N) - 1) * 9)
        exit()
print(int(N[0]) + (len(N) - 1) * 9)