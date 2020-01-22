N = int(input())
A = list(map(int, input().split()))
A = [(a, i) for i, a in enumerate(A)]
A.sort(reverse=True)
for a in A:
    print(a[1] + 1)