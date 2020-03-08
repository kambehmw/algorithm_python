N, P = map(int, input().split())
S = input()
numMultiples = 0
seenRemainders = [set() for _ in range(N)]
for i in range(N):
    remainder = 0
    prefixesFound = 0
    for j in range(i, N):
        remainder = (10 * remainder + int(S[j])) % P
        if remainder in seenRemainders[j]:
            break
        seenRemainders[j].add(remainder)
        if remainder == 0:
            prefixesFound += 1
    numMultiples += prefixesFound * (prefixesFound + 1) // 2
print(numMultiples)