a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
for x in [a, b, c, d, e]:
    for y in [a, b, c, d, e]:
        if x != y:
            if k < abs(x - y):
                print(":(")
                exit()
print("Yay!")