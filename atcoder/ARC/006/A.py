E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))
set_E = set(E)
set_L = set(L)
cnt = len(set_E.intersection(set_L))
bonus = True if B in set_L else False
if cnt == 6:
    print(1)
elif cnt == 5:
    if bonus:
        print(2)
    else:
        print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)