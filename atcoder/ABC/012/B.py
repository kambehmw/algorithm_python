N = int(input())
second = N % 60
minute = N // 60
hour = minute // 60
minute = minute % 60
print("{:0=2}:{:0=2}:{:0=2}".format(hour, minute, second))
