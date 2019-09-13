SA = input()
SB = input()
SC = input()
turn = SA[0]
while True:
    if turn == "a":
        turn = SA[0]
        SA = SA[1:]
    elif turn == "b":
        turn = SB[0]
        SB = SB[1:]
    elif turn == "c":
        turn = SC[0]
        SC = SC[1:]
    if turn == "a" and not SA:
        print("A")
        exit()
    elif turn == "b" and not SB:
        print("B")
        exit()
    elif turn == "c" and not SC:
        print("C")
        exit()