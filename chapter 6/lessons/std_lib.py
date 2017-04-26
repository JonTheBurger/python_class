# Lesson 1
# The standard library allows us to work with directories
import os
import time
import datetime

print('Hello,', os.getlogin())
print('This script is running from', os.getcwd())
dir_name = 'temp'

# isdir checks if the provided string is a directory
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

os.chdir(dir_name)
print("Now we're in", os.getcwd())

# makedirs makes multiple directories. it will crash if they exist!
os.makedirs('my/cool/dir')
os.chdir('my/cool/dir')

# we can use relative paths
os.chdir('..')
print("Now we're in", os.getcwd())

os.rmdir('dir')
os.chdir('../../..')

# time and datetime are useful as well
# module.class.method()
# now tells us the current time
print(datetime.datetime.now())
# sleep delays the program for n seconds
time.sleep(2)
print(datetime.datetime.now())
time.sleep(2)
print(datetime.datetime.now())
