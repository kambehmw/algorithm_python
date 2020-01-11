S = input()
T = input()
length = len(T)
results = []
for i in range(len(S)-length+1):
    flag = True
    for s, t in zip(S[i:i+length], T):
        if s == "?":
            continue
        if s != t:
            flag = False
            break
    if flag:
        results.append(S[:i] + T + S[i+length:])

if len(results) == 0:
    print("UNRESTORABLE")
else:
    results = [res.replace("?", "a") for res in results]
    results.sort()
    print(results[0])