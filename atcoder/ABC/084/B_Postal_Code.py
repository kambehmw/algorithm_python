import re
A, B = map(int, input().split())
S = input()
postal = "^\d{{{}}}-\d{{{}}}$".format(A, B)
is_postal = re.match(postal, S)
if is_postal:
    print("Yes")
else:
    print("No")