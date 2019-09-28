from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
start = 1 if N % 2 == 0 else 0
if N % 2 == 0:
    if counter[start] != 2:
        print(0)
        exit()
else:
    if counter[start] != 1:
        print(0)
        exit()

for i in range(start+2, N, 2):
    if counter[i] != 2:
        print(0)
        exit()
print(2 ** (N // 2) % (10**9 + 7))
