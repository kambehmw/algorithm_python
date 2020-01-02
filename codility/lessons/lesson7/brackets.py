def solution(S):
    stack = []
    for c in S:
        if c in (")", "}", "]"):
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
                if c == ")":
                    if tmp != "(":
                        return 0
                elif c == "}":
                    if tmp != "{":
                        return 0
                elif c == "]":
                    if tmp != "[":
                        return 0
        else:
            stack.append(c)

    if len(stack) != 0:
        return 0
    return 1

if __name__ == '__main__':
    S = "{[()()]}"
    print(solution(S))

    S = "{[()()]"
    print(solution(S))