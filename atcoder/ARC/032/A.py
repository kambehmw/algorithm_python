n = int(input())
if n == 1:
    print("BOWWOW")
    exit()
total = sum(range(1, n+1))
for i in range(2, total):
    if total % i == 0:
        print("BOWWOW")
        exit()
print("WANWAN")