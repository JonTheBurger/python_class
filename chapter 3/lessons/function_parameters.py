# Lesson 4


def times2(x):
    return x * 2


# Functions can also be passed into functions. In this case we pass in "transformation()"
def transform(items, transformation):
    for i in range(len(items)):
        items[i] = transformation(items[i])


numbers = [1, 2, 3, 4, 5]
transform(numbers, times2)
for num in numbers:
    print(num)
