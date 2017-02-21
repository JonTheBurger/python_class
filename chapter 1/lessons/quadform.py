# Lesson 6

import math     # we're going to use python's math library

print('Quadratic solver')
# floats are numbers with decimal points
a = float(input('a: '))   # e.g. 1
b = float(input('b: '))   # e.g. 2
c = float(input('c: '))   # e.g. -8

d = b ** 2 - 4 * a * c
e = -b + math.sqrt(d)   # here we're calling a function inside of math
f = -b - math.sqrt(d)
x1 = e / 2 / a
x2 = f / 2 / a

print('x =', x1, ' and', x2)
