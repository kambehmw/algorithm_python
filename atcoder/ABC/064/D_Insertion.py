import copy
N = int(input())
S = input()
stack = []
ans = copy.deepcopy(S)
for s in S:
    if s == ")":
        if len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        else:
            ans = "(" + ans
    elif s == "(":
        stack.append(s)
for _ in range(len(stack)):
    ans = ans + ")"
print(ans)