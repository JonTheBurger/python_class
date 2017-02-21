# Lesson 5

first_name = input('First name: ')
last_name = input('Last name: ')

# we can use + to combine, or 'concatenate', strings.
full_name = first_name + ' ' + last_name
print('Your full name is', full_name)

# we can compare strings using ==
if first_name == 'Steve':
    print('Your name is Steve? What a great name!')

# we can call the len() function on a string to get its length in characters.
print('Your first name is', len(first_name), 'letters long.')

# we can multiply a string by an int to repeat it.
# Operators follow the same precedence as they do in math.
verys = 'very ' * 5
print('Python is ' + verys + 'cool.')
