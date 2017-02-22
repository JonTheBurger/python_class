# Lesson 4

# calling print() on list iterates over it for you and adds brackets!
list = [0, 1, 3, 2, 3, 4]
print(list)

# We can add to lists like so
list += [5, 6, 7, 8, 9]
print(list)

# List has plenty of utility functions built in

print('Reversed')
for x in reversed(list):
    print(x, end=' ')
print()

# Remove removes the first instance of the specified value from a list
print('Remove 3')
list.remove(3)
print(list)

# We can call len() on lists too
print('Len of list:', len(list))

# [] allows you to index into a list. List indexing starts at 0.
print('First item:', list[0])
print('Third item:', list[2])

# Using a negative number indexes from the end of the list.
print('Last item:', list[-1])
print('Second last item:', list[-2])

# Using colon allows us to select multiple items. [elements to skip, stop before this element]
print('First 2 items:', list[0:2])
print('First 2 items:', list[:2])   # if we skip 0, we can start with a colon

print('All but first and last:', list[1:-1])
print('All but first:', list[1:])   # if we take all after a skip, we end with a colon

# Lists can be sorted too
l = [5, 2, 7, 4]
l.sort()
print(l)
