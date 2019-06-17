stack = []

def push(x):
    stack.append(x)

def pop():
    return stack.pop()

def main():
    ops = input().split()
    
    for op in ops:
        print(stack)
        if op == "+":
            push(pop() + pop())
        elif op == "-":
            push(-pop() + pop())
        elif op == "*":
            push(pop() * pop())
        else:
            push(int(op))
    print(pop())

if __name__ == '__main__':
    main()