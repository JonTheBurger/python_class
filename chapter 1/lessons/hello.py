# Lesson 1
# This is a comment. It's ignored by the Python interpreter.
# We use comments to document our code.
"""
This is
a multi-line
comment.
"""

# We can use the print function to display text to the terminal.
print('hello world!')

# This declares a "variable" named 'num' with the value 5.
num = 5
# Numbers can be printed too.
print(num)

# Variables can be reassigned.
num = 6
# When we pass a value to a function, it is called an "argument", that is num is an argument to the print function.
print(num)

# We can make variables that hold text too. These are called "strings".
name = 'bob'
print(name)

# We can't add an number to a string!
# name = 'bob' + 2  # Not allowed!

# The input function reads text from the terminal. It's argument prints a prompt to the screen for the user.
name = input('What is your name? ')

# We can use + to combine, or "concatenate" strings.
print('Hello, ' + name + '!')
