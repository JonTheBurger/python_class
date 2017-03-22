# Lesson 1


def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iterative_factorial(5))


# "Recursion" is the act of calling a function from within itself. Some functions naturally work better recursively.
# Recursion is easier to work out if you write it down on paper.
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:   # Recursive functions generally have a "base case", from which they stop recursing.
        return 1
# NOTE: It's helpful to draw out the "frames" of each function call

print(factorial(5))
