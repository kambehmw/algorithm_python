N = int(input())
A = list(map(int, input().split()))
s = set(A)
k = len(s)
if k % 2 == 0:
    print(k - 1)
else:
    print(k)