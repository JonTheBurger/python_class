# Lesson 4

# Dictionaries are sets of distinct "keys", each with a value.
person_to_age = {'Alice': 25, 'Bob': 30, 'Carol': 10, 'Dave': 25}

# We use [] to access a key's value in a dictionary
alice_age = person_to_age['Alice']
print('Alice is', alice_age)


# We can use Dictionary.items() to a tuple of (key, value) present in a dictionary. We can also get keys() and values().
for key, value in person_to_age.items():
    print(key, 'is', value)
print()


# We can also use [] to create a new key value pair.
person_to_age['Eve'] = 29
for key, value in person_to_age.items():
    print(key, 'is', value)
print()


# To remove a key, we use pop()
person_to_age.pop('Alice')
for key, value in person_to_age.items():
    print(key, 'is', value)
