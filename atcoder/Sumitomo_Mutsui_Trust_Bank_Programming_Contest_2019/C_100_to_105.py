X = int(input())
div = X // 100
mod = X % 100
if 0 <= mod <= div * 5:
    print("1")
else:
    print("0")
