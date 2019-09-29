S = input()
T = input()
for i in range(len(S)):
    if S[len(S)-i-1] != T[i]:
        print("NO")
        exit()
print("YES")