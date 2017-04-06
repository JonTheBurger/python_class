# Lesson 1
# Polymorphism allows us to model an "is-a" relationship between classes


class Shape:
    # Shapes have an area
    def area(self):
        pass


# Here, Rectangle "extends", or "derives from" Shape. A Rectangle is a Shape.
# Shape is called the "base class", "parent class", or "super class"
# Rectangle is called the "derived class", "child class", or "sub-class"
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # We want to make sure we implement the methods in the base class
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2


# This function expects an instance of Shape, or one of its derivatives. Shape is used "polymorphically"
def print_area(shape):
    if isinstance(shape, Shape):
        print(shape.area())


# We can also use classes for code reuse, but we should prefer making rectangle a member if we aren't using this class
# as a polymorphic rectangle. Extension will be shown for the sake of example.
class DrawableRectangle(Rectangle):
    def __init__(self, length, width):
        # Call our "parent" class, or "super"'s init method to ensure that our base class is properly initialized.
        super(DrawableRectangle, self).__init__(length, width)

    def draw(self):
        for l in range(0, self.length):
            for w in range(0, self.width):
                print('*', end='')
            print()


def main():
    rect = Rectangle(2, 3)
    circle = Circle(4)
    drawable = DrawableRectangle(3, 4)

    # notice that DrawableRectangle is still a shape!
    for shape in [rect, circle, drawable]:
        print_area(shape)

    drawable.draw()

if __name__ == '__main__':
    main()
