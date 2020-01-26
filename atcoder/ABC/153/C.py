N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
# print(H)
if K != 0:
    H = H[:-K]
ans = sum([x for x in H])
print(ans)