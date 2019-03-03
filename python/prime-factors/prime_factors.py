def prime_list(integer):
    '''implementation of the sieve of Eratosthenes'''
    limit = integer + 1
    sieve = {}
    for i in range(2,limit):
        sieve[i] = True # Setting all values to true
    for i in sieve:
        factor = range(i,limit,i) # iterate through i's multiples
        for j in factor[1:]: # Every multiple but inital number
            sieve[j] = False # set false, it must be a multiple
    return [ i for i in sieve if sieve[i]==True ] # return primes list

def divides_cleanly(numerator,denominator):
    if numerator % denominator == 0:
        return True
    return False

def prime_factors(natural_number):
    myNumber = natural_number
    myPrimes = prime_list(1000000)
    factors = []
    for i in myPrimes:
        if divides_cleanly(myNumber,i):
            while divides_cleanly(myNumber,i) == True:
                factors.append(i)
                myNumber = int(myNumber / i)
    return factors
