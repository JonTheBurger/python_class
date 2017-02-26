# Lesson 5

# This declares an empty list
inputs = []

# This reads like plain old English. While the length of our input is less than 5...
while len(inputs) < 5:
    x = input('Next: ')
    inputs += [x]   # We must put x in a list to append it
    # inputs.append(x)  # We can also append this way

print(inputs)

iterations = 1
# This will loop forever
while True:
    y = input('Type "stop" to quit')
    # This is a compound addition. It is equivalent of writing iterations = iterations + 1
    iterations += 1     # Compound operators exist for most mathematical operations (e.g. -= *= /= %= **= etc.)
    if y == 'stop':
        break           # The "break" statement will exit the inner-most loop containing it

print('iterations run: ' + iterations)
