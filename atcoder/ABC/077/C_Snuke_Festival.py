import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
    i = bisect.bisect_left(A, b)
    j = bisect.bisect_right(C, b)
    ans += i * (N - j)
print(ans)