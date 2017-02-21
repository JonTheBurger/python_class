# Lesson 4

x = int(input('x: '))

remainder = x % 2

"""
    We can make the following numerical comparisons:
    == if equal
    != not equal
    >= greater than or equal to
    <= less than or equal to
    >  greater than
    <  less than
"""

# If statements are used to conditionally execute code based on a boolean expression.
if remainder == 0:
    print('x is even')
else:
    print('x is odd')
