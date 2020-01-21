day = input()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if day == "Saturday" or day == "Sunday":
    print(0)
else:
    print(days.index("Saturday") - days.index(day))