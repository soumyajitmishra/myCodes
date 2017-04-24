# This program is to find out prime numbers between 0 to 100
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for divisor in range(3, n, 1):
        if n % divisor == 0:
            return False
    return True

for i in range(100):
    primeNo = is_prime(i)
    if primeNo == True:
        print "%d is a Prime no" % i
    else:
        print "%d is not a Prime no" % i

