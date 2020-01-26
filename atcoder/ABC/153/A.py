H, N = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
if H <= total:
    print("Yes")
else:
    print("No")