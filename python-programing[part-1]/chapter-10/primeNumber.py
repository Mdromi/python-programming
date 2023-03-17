# python3 chapter-10/primeNumber.py

import math
import timeit

def isPrime(n=1013):
    if n == 2:
        return True # 2 is  prime
    if n % 2 == 0:
        print(n, 'is divisible by 2')
        return False # all even numbers except 2 are not prime
    if n < 2:
        return False # numbers less then 2 are not prime

    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            print(n, 'is divisible by', x)
            prime = False
            return prime

    return prime  

def isPrime2(n=1013):
    if n < 2:
        return fa;se
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    m = math.sqrt(n)
    m = int(m) + 1

    for x in range(3, m, 2):
        if n % 2 == 0:
            return False
    return True

while False:
    number = input('Please enter a number (enter 0 to exit): ')
    number = int(number)

    if number == 0:
        break
    prime = isPrime(number)
    if prime is True:
        print(number, 'is a prime number.')
    else:
        print(number, 'is not a prime number.')


t1 = timeit.timeit(isPrime)
t2 = timeit.timeit(isPrime2)
print(t1, t2, t1/t2)

