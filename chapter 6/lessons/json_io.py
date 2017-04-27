# Lesson 6
# json, or "Javascript Object Notation" is a common object interchange format in the world of the web.
import json

people = {
    'sagget': 'bob',
    'buscemi': 'steve',
    'stewart': 'martha',
}

# We can json serialize dictionaries no problem!
print(json.dumps(people))


# We can use the dictionary present in every python object to serialize
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

greg = Person('greg', 28)
amy = Person('amy', 24)
print(json.dumps([greg.__dict__, amy.__dict__]))


# And we can assign the dictionary of a dummy object to deserialize
class AnonymousJson:
    def __init__(self, j):
        self.__dict__ = json.loads(j)

greg_json = json.dumps(greg.__dict__)
print(greg_json)
g2 = AnonymousJson(greg_json)
print(g2.name)
print(g2.age)
