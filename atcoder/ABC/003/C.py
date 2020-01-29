N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
rate = 0
for r in R[-K:]:
    rate = (rate + r) / 2
print(rate)
