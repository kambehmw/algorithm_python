import math


def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x))) / p


deg, dis = map(int, input().split())
deg *= 10
if 1125 <= deg < 3375:
    d = "NNE"
elif 3375 <= deg < 5625:
    d = "NE"
elif 5625 <= deg < 7875:
    d = "ENE"
elif 7875 <= deg < 10125:
    d = "E"
elif 10125 <= deg < 12375:
    d = "ESE"
elif 12375 <= deg < 14625:
    d = "SE"
elif 14625 <= deg < 16875:
    d = "SSE"
elif 16875 <= deg < 19125:
    d = "S"
elif 19125 <= deg < 21375:
    d = "SSW"
elif 21375 <= deg < 23625:
    d = "SW"
elif 23625 <= deg < 25875:
    d = "WSW"
elif 25875 <= deg < 28125:
    d = "W"
elif 28125 <= deg < 30375:
    d = "WNW"
elif 30375 <= deg < 32625:
    d = "NW"
elif 32625 <= deg < 34875:
    d = "NNW"
else:
    d = "N"

# print(dis / 60)
v = my_round(dis / 60, 1)
# print(v)
if 0.0 <= v <= 0.2:
    print("C", 0)
elif 0.3 <= v <= 1.5:
    print(d, 1)
elif 1.6 <= v <= 3.3:
    print(d, 2)
elif 3.4 <= v <= 5.4:
    print(d, 3)
elif 5.5 <= v <= 7.9:
    print(d, 4)
elif 8.0 <= v <= 10.7:
    print(d, 5)
elif 10.8 <= v <= 13.8:
    print(d, 6)
elif 13.9 <= v <= 17.1:
    print(d, 7)
elif 17.2 <= v <= 20.7:
    print(d, 8)
elif 20.8 <= v <= 24.4:
    print(d, 9)
elif 24.5 <= v <= 28.4:
    print(d, 10)
elif 28.5 <= v <= 32.6:
    print(d, 11)
else:
    print(d, 12)
