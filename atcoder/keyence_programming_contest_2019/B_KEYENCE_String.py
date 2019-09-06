S = input()
for i in range(len(S)-1):
    for j in range(i, len(S)):
        partial_str = S[:i] + S[j:]
        if partial_str == "keyence":
            print("YES")
            exit()
print("NO")