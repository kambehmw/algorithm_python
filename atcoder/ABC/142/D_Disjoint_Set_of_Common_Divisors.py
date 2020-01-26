import math

def is_prime(n):
    if n == 1: return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

A, B = map(int, input().split())
div1 = make_divisors(A)
# print(div1)
div2 = make_divisors(B)
nums = list(set(div1).intersection(set(div2)))
# print(nums)
nums = [x for x in nums if is_prime(x)]
# print(nums)
cnt = len(nums)
if cnt > 1:
    print(cnt)
else:
    print(1)