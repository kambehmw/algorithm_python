N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

max_price = max(P)
max_index = P.index(max_price)
del P[max_index]
print(sum(P) + int(max_price / 2))