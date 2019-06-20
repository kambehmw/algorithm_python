"""
Constraints:
    - 1<= a, b <= 10000
    - a nd b are integer
"""
import time

def is_even(int_num):
    if int_num % 2 == 0:
        return True
    else:
        return False


def main():
    # start = time.time()
    inputs = input().split()
    a, b = int(inputs[0]), int(inputs[1])
    if is_even(a * b):
        print("Even")
    else:
        print("Odd")

    # print((time.time() - start) * 1000.0)

if __name__ == "__main__":
    main()
