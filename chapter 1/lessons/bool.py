# Lesson 3

age = int(input('How old are you? '))

# is_adult is a "boolean" variable. It can store either "True" or "False".
# >= is a "comparison operator". It reads "greater than or equal to".
is_adult = (age >= 18)
print('You are an adult:', is_adult)

is_senior = (age >= 65)
print('You are a senior:', is_senior)

# Comparison operators can be combine
is_teenager = (13 <= age <= 19)
print('You are a teenager:', is_teenager)
