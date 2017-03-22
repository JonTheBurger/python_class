# Lesson 5


# Classes allow us to define our own types. A class is simply a way to package related data members together and call
# useful functions on said data.
class Rectangle:
    # Functions that begin and end with __ are "magic methods" reserved by Python.
    # The init function is used to initialize and return an instance of your Rectangle class.

    # self refers to the current instance of Rectangle.
    #  (self is just a naming convention. In reality, the first parameter is what refers to the current instance.)
    def __init__(self, length, width):
        self.length = length    # Create member variables length and width.
        self.width = width

    # Create member function area. Notice that self (the current rectangle) is always passed as the first parameter.
    def area(self):
        return self.length * self.width

rect = Rectangle(2, 3)
print(rect)
print(rect.area())
