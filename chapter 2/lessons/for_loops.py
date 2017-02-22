# Lesson 3

# The for loop lets you iterate over a string
for letter in 'Python':
    print(letter, end='! ')  # sep lets us replace the newline usually put after a print() with whatever we want!
# An empty print simply prints a newline
print()

# Putting items between [] creates a list, which can also be iterated over via for loops
for number in [1, 2, 3, 4, 5]:
    print(number)

# We can even make lists of strings, or lists of more lists!
for word in ['Hello', 'how', 'are', 'you?']:
    print(word)

for sub_list in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print('sub_list start:')
    for item in sub_list:
        print(item)
