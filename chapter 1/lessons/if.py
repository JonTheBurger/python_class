# Lesson 4

x = int(input('x: '))

if x < 0:
    print('x is negative')
elif x > 0:
    print('x is positive')
else:
    pass    # The 'pass' statement lets us do nothing within a control structure.

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

remainder = x % 2
if remainder == 0:
    print('x is even')
else:
    print('x is odd')
