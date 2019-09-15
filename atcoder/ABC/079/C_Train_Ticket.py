ABCD = input()
A, B, C, D = [int(x) for x in ABCD]
ops = ["+", "-"]
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            if op1 == "+":
                ans = A + B
            else:
                ans = A - B
            if op2 == "+":
                ans += C
            else:
                ans -= C
            if op3 == "+":
                ans += D
            else:
                ans -= D
            if ans == 7:
                print(str(A) + op1 + str(B) + op2 + str(C) + op3 + str(D) + "=" + str(ans))
                exit()
