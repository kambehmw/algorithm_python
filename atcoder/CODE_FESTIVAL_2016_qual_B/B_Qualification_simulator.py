N, A, B = tuple(map(int, input().split()))
S = input()
count = 0
abroad_rank = 1
for c in S:
    if c == "a":
        if count < A + B:
            count += 1
            print("Yes")
        else:
            print("No")
    elif c == "b":
        if count < A + B and abroad_rank <= B:
            count += 1
            abroad_rank += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
