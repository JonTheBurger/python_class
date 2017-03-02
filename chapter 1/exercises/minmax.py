# Exercise 2
# Preq: Lesson 4

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

smallest = x
if y < smallest:
    smallest = y
if z < smallest:
    smallest = z

biggest = x
if y > biggest:
    biggest = y
if z > biggest:
    biggest = z

print('min:', smallest)
print('max:', biggest)

# We can also use the min and max functions
print('min:', min(x, y, z))
print('min:', max(x, y, z))
