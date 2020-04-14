A, B = map(int, input().split())
cnt1 = B // 4 - (B // 100 - B // 400)
A -= 1
cnt2 = A // 4 - (A // 100 - A // 400)
print(cnt1 - cnt2)