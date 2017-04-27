# Lesson 3
import os


def better_be_5(value):
    if value != 5:
        # Exceptions provide us a way to change control flow on errors. We use them when we want to force the
        # programmer to deal with a problem, or otherwise crash
        raise ValueError('Value must be 5!')


better_be_5(5)
try:
    # The try statement says "I expect an exception to be thrown in here"
    better_be_5(4)
except ValueError as e:
    # The except statement here says "I can handle an exception of the type ValueError (or a derived type) and call that
    # exception e"
    print(e)

for _ in range(3):
    try:
        os.chdir('asdfjkl')
    except Exception as e:
        # All exceptions are derived from Exception, so this will effectively catch any type of Exception.
        print(e)


# What if our program crashes from an exception while we have a file open? Only 1 process is allowed to touch a file at
# a time! It could leak the file handle!

# The with statement will cleanup resources even if an exception goes unhandled! However, it does not handle the
# exception for us--it only prevents resource leaks!
with open('file.txt', 'w') as f:
    raise Exception
