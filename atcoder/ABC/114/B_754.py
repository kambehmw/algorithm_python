S = input()
diff = []
for i in range(len(S)-3+1):
    num = int(S[i:i+3])
    diff.append(abs(753 - num))
print(min(diff))