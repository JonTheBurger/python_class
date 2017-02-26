# Lesson 2
from collections import namedtuple

# Sometimes we want to return multiple values. This can be achieved with tuples.
def get_line(x0, y0, x1, y1):
    """ Returns m and b of y = mx + b equation for the provided points. """
    m = (y1 - y0) / (x1 - x0)
    b = y0 - m * x0     # y = mx + b -> y - mx = b
    return m, b

slope, intercept = get_line(0, 4, 2, 8)
print('y =', slope, 'x +', intercept)
print()

# By convention, if we don't care about one of the tuple outputs of a function, we make a variable named _
_, intercept = get_line(1, 4, 6, 9)     # e.g. we don't care about the slope.


# We can also declare tuples
my_tuple = (1, 2)
print(my_tuple)
print(my_tuple[0])  # We index into tuples in a manner similar to lists
print(my_tuple[1])
print()

# We can use named_tuple for better readability
# Here we declare a namedtuple type "Point", named "point", with fields "x" and "y"
Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)  # We access the fields of our named tuple with the dot operator
print(p.y)
