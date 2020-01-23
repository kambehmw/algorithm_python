A, B = map(int, input().split())
ans = float('-inf')
str_A = str(A)
A1 = "9" + str_A[1:]
ans = max(ans, int(A1) - B)
A2 = str_A[0] + "9" + str_A[2]
ans = max(ans, int(A2) - B)
A3 = str_A[:2] + "9"
ans = max(ans, int(A3) - B)
str_B = str(B)
B1 = "1" + str_B[1:]
ans = max(ans, A - int(B1))
B2 = str_B[0] + "0" + str_B[2]
ans = max(ans, A - int(B2))
B3 = str_B[:2] + "0"
ans = max(ans, A - int(B3))
print(ans)