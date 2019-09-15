O = input()
E = input()
ans = ""
for o, e in zip(O, E):
    ans += o
    ans += e
if len(O) > len(E):
    ans += O[-1]
elif len(O) < len(E):
    ans += E[-1]
print(ans)