# python3 chapter-2/program.py

import fibo
import trail
import sys

print('Hello, I am inside program.py')

n = fibo.find_fib(15)

print('15 fibonacci number is,', n)
print(trail.__name__)

print(sys.path)