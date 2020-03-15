N = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

divs = make_divisors(N)
divs.sort()
total = sum(divs[:-1])
if total < N:
    print("Deficient")
elif N < total:
    print("Abundant")
else:
    print("Perfect")