S1 = input()
S2 = input()
S3 = input()
S = [S1, S2, S3]
N = len(S1)
C = [[0] * 26 for _ in range(3)]
for i in range(3):
    for c in S[i]:
        C[i][ord(c) - ord("A")] += 1

low, high = 0, 0
for i in range(26):
    if C[0][i] + C[1][i] < C[2][i]:
        print("NO")
        exit()
    low += max(0, C[2][i] - C[1][i])
    high += min(C[0][i], C[2][i])

if low <= N // 2 <= high:
    print("YES")
else:
    print("NO")
