S = input()
d = {"O": "0", "D": "0", "I": "1", "Z": "2", "S": "5", "B": "8"}
print("".join([d[s] if s in d else s for s in S]))