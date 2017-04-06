# Lesson 4
class Distance:
    _KM_PER_MILE = 0.621371

    def __init__(self, distance, unit):
        self._distance = distance
        self._unit = unit

    def to_kilometers(self):
        if self._unit == 'mi':
            return self._distance * self._KM_PER_MILE
        else:
            return self._distance

    def to_miles(self):
        if self._unit == 'km':
            return self._distance * (1 / self._KM_PER_MILE)
        else:
            return self._distance

    # operator overloading allows us to use native symbols like == or + to call custom methods
    def __eq__(self, other):
        return self.to_kilometers() == other.to_kilometers()

    def __add__(self, other):
        return Distance(self.to_kilometers() + other.to_kilometers(), 'km')

d0 = Distance(10, 'km')
print(d0.to_kilometers())
print(d0.to_miles())

d1 = Distance(3, 'km')
d2 = d0 + d1            # calls __add__
print(d2.to_kilometers())
print(d2 == (d0 + d1))  # calls __eq__
