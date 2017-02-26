# Lesson 3

# A "set" is an unordered collection of unique items. They are declared with "braces".
# You cant hink of them as venn-diagrams.
s = {1, 2, 3, 4, 5, 4, 3, 2, 1}
print(s)
s.add(20)           # We can add to a set with the add() method.
s.update([5, 10, 30])  # We can add a collection with update. Notice that the redundant 5 is not added to the set!
print(s)
print()

# We can also create sets from lists
from_list = set([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(from_list)
print()


# Set has useful operations like "issubset" and "issuperset". This allows us to apply set theory operations!
primes = {2, 3, 5, 7, 11, 13, 17, 19}
numbers = {2, 3, 5}
print(numbers.issubset(primes))
print()

# We can use discard() to remove an item from the set if it exists. If it doesn't exist, it's ignored.
numbers.discard(3)
print(numbers)
