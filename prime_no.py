# This program is to find out prime numbers between 0 to 100
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for divisor in range(3, n, 1):
        if n % divisor == 0:
            return False
    return True

# Declaring two blank lists to store prime and non-prime numbers
primeList = []
nonPrimeList = []

for i in range(100):
    primeNo = isPrime(i)
    if primeNo == True:
        primeList.append(i)
    else:
        nonPrimeList.append(i)

print "Prime numbers between 0 to 100 are: ", primeList
print "Non Prime numbers between 0 to 100 are: ", nonPrimeList
