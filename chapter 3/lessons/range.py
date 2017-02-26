# Lesson 1

# The range function generates the sequence of numbers from [start, end). Notice end is NOT included.
start = 1
end = 10
for i in range(start, end):
    print(i)
print()

# The optional step parameter
step = 2
for i in range(start, end, step):
    print(i)
print()

# We can also generate ranges in "reverse"
for i in range(10, 0, -1):
    print(i)
