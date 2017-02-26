# Lesson 2


# This declares a "function". A functions inputs, in this case "x", are called "parameters"
def squared(x):
    # The "return" statement defines the output of a function.
    return x ** 2

# A function input that satisfies a parameter is called an "argument".
# Many people use argument and parameter interchangeably, which is fine.
print(squared(2))


def say_hello():
    # If a function contains no return statement, it returns None.
    print('hello')

output = say_hello()
print(output)


# Functions can call other functions
def cubed(x):
    return squared(x) * x

# print() is a function provided by Python!
print(cubed(3))
