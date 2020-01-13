m = int(input())
m = m / 1000.0
if m < 0.1:
    print("00")
elif m <= 5:
    m *= 10
    if m < 10:
        print("0" + str(int(m)))
    else:
        print(str(int(m)))
elif 6 <= m <= 30:
    print(int(m + 50))
elif 35 <= m <= 70:
    print(int((m - 30) / 5 + 80))
elif 70 < m:
    print(89)