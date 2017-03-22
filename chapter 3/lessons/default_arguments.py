# Lesson 3


# If arguments n3 or later aren't provided by the caller, they'll use a default value instead
def add(n1, n2, n3=0, n4=0, n5=0, n6=0):    # (We'll learn a better way to do something like this later)
    return n1 + n2 + n3 + n4 + n5 + n6

print(add(1, 2, 3, 4))

# We can explicitly fulfil arguments out of order by using "named parameters"
print(add(n2=1, n1=4, n6=3))
