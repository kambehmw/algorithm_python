S = input()
for i in range(2, len(S), 2):
    part_S = S[:-i]
    # print(part_S)
    mid = len(part_S) // 2
    left_S = part_S[:mid]
    right_S = part_S[mid:]
    if left_S == right_S:
        print(len(part_S))
        exit()
