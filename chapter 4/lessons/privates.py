# Lesson 6


# Sometimes, we want to protect some of the data or methods in our classes
class RestroomStall:
    def __init__(self):
        self._occupants = 0         # protected variables discourage use
        self.__bathroom_cam = 0     # private variables prevent use

    def is_occupied(self):
        return self._occupants != 0

    def enter(self):
        if not self.is_occupied():
            print('You have entered the bathroom')
            self._occupants += 1
        else:
            print("You can't enter the bathroom, it's occupied!")

    def exit(self):
        if self.is_occupied():
            print("You're exiting the bathroom")
            self._occupants -= 1
        else:
            print('ERROR! Attempted restroom exit with 0 occupants!')

stall = RestroomStall()
stall.enter()
stall.exit()

stall.enter()
stall.enter()
# If we really need to, we can access protected variables,
# but the class author is trying to tell you that modification is dangerous!
stall._occupants = 0
stall.enter()
# However, we cannot access private variables!
stall.__bathroom_cam
