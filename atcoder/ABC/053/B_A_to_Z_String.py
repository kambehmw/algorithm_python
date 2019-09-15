S = input()
i = 0
start = 0
while True:
    if S[i] == "A":
        start = i
        break
    i += 1

i = -1
end = 0
while True:
    if S[i] == "Z":
        end = i + 1
        break
    i -= 1

if end < 0:
    print(len(S[start:end]))
else:
    print(len(S[start:]))