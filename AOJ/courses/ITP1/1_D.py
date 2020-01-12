S = int(input())
minute = S // 60
hour = minute // 60
minute = minute % 60
second = S % 60
print("{}:{}:{}".format(hour, minute, second))