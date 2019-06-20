"""
Constraints:
    - 1<=a,b<=100
    - a and b are integers

"""

import time

def is_squared(num):
    i = 4
    while True:
        squred_num = i * i
        if num == squred_num:
            return True
        if squred_num > num:
            return False
        i += 1



def main():
    inputs = input().split()
    if len(inputs) != 2:
        print("input is invalid. input two integers.")
        exit(1)

    a, b = inputs[0], inputs[1]
    if not (1 <= int(a) <= 100) or not (1 <= int(b) <= 100):
        print("input is invalid. input two integers. (1<=a,b<=100) ")

    # start = time.time()
    cat_num = int(a + b)
    if is_squared(cat_num):
        print("Yes")
    else:
        print("No")
    # print(time.time() - start)


if __name__ == '__main__':
    main()

