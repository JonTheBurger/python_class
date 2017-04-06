# Lesson 3
class Person:
    def __init__(self, fname, lname):
        self._fname = fname
        self._lname = lname

    # properties allow us to emulate member variables with correctional logic
    @property
    def full_name(self):
        return self._fname + ' ' + self._lname

    # we can also use them to assert that an attempted write to a member is valid
    @full_name.setter
    def full_name(self, name):
        if name is None:
            return
        parts = name.split(' ')
        # if some_string will evaluate to true if it is not None and not empty
        if len(parts) >= 2 and parts[0] and parts[1]:
            self._fname = parts[0]
            self._lname = parts[1]

person = Person('Donald', 'Duck')
print(person.full_name)

# The property will protect against an invalid name
person.full_name = 'MickeyMouse'
print(person.full_name)

person.full_name = 'Mickey Mouse'
print(person.full_name)
