X = input()
stack = []
for x in X:
    if x == "S":
        stack.append(x)
    elif x == "T":
        if len(stack) == 0 or stack[-1] == "T":
            stack.append(x)
        elif stack[-1] == "S":
            stack.pop()
print(len(stack))
