# Lesson 5

# This declares an empty list
inputs = []

# This reads like plain old English. While the length of our input is less than 5...
while len(inputs) < 5:
    x = input('Next: ')
    inputs += [x]   # We must put x in a list to append it
    # inputs.append(x)  # We can also append this way

print(inputs)
