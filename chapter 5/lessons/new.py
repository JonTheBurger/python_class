# Lesson 5


# When deriving read-only classes like int, we can override __new__ to change how new instances are generated.
# This can be useful if you ever need to deal with raw byte streams.
class MyInt(int):
    def __new__(cls, *args, **kwargs):
        return 5

i = MyInt()
print(i)
print(type(i))
