# Lesson 2
import os

# open opens a file
# 'w' creates a new file (overwrites an existing file), a appends, r reads. r+ allows reading and writing
f = open('store.txt', 'w')

# we can use write to write strings
f.write('Hello!\n')
f.write('We can use files to store state across program uses!\n')
f.write(str(12345))

# close the file when you're done with it!
f.close()
# the closed property returns a boolean value
print(f.closed)

# print all of the contents of the file
f = open('store.txt', 'r')
print(f.read())
f.close()
print('...')

# or print line by line
# notice we close and reopen the file here. That's because after we read all of the lines, the read cursor is at the end
# of the file.
f = open('store.txt', 'r')
for line in f:
    print(line)
f.close()

# We can use os to delete files as well
os.remove('store.txt')
