# Lesson 2

# The int function converts a string to an integral number.
x = int(input('x: '))
y = int(input('y: '))

ans = x + y
print('x + y =', ans)     # If we send multiple arguments to the print function, it will put a space between them.

ans = x - y
print('x - y =', ans)

ans = x * y
print('x * y =', ans)

ans = x / y
print('x / y =', ans)

ans = x // y    # with floor division, we throw out the remainder.
# E.g. 5 // 2 can be read as '5 can be evenly divided into 2 groups -> 2 times'
print('x // y =', ans)

ans = x % y     # with modulus, we take the remainder of a division
# E.g. 5 % 2 can be read as '5 divided into even groups of 2 leaves a remainder of -> 1'
print('x % y =', ans)

ans = x ** y    # with exponent, we take x to the y (x^y)
print('x ** y =', ans)

ans = x + y / 2     # in Python, operator precedence follows the same rules as regular math.
print('x + y / 2 =', ans)

ans = (x + y) / 2
print('(x + y) / 2 =', ans)  # we can use parenthesis just like in math for precedence.
