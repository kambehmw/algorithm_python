from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
rate_dict = defaultdict(int)
for a in A:
    if 1 <= a <= 399:
        rate_dict["gray"] += 1
    elif 400 <= a <= 799:
        rate_dict["brown"] += 1
    elif 800 <= a <= 1199:
        rate_dict["green"] += 1
    elif 1200 <= a <= 1599:
        rate_dict["light_blue"] += 1
    elif 1600 <= a <= 1999:
        rate_dict["blue"] += 1
    elif 2000 <= a <= 2399:
        rate_dict["yellow"] += 1
    elif 2400 <= a <= 2799:
        rate_dict["orange"] += 1
    elif 2800 <= a <= 3199:
        rate_dict["red"] += 1
    elif 3200 <= a:
        rate_dict["free"] += 1
ans = sum([1 if x in rate_dict else 0
           for x in ["gray", "brown", "green", "light_blue", "blue", "yellow", "orange", "red"]])
min_ans = ans
if "free" in rate_dict:
    if len(set(list(rate_dict.keys()))) == 1:
        min_ans = 1
    max_ans = ans + rate_dict["free"]
else:
    max_ans = min_ans
print("{} {}".format(min_ans, max_ans))
