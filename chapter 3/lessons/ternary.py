# Lesson 5

n = int(input('Input a number: '))

# This is the "ternary operator". It allows us to conditionally use a value.
non_negative = 0 if n < 0 else n
print(non_negative)

# Long version of ternary operator:
if n < 0:
    non_negative = 0
else:
    non_negative = n
