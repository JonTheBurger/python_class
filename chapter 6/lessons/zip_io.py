# Lesson 5
# Zip files allow us to compress files and directories
import zipfile

with open('example.txt', 'w') as f:
    f.write('Hi! This file will be compressed!')

with zipfile.ZipFile('example.zip', 'w') as z:
    z.write('example.txt')  # add file to zip archive

with zipfile.ZipFile('example.zip', 'r') as z:
    f = z.read('example.txt')
    # Zipfiles are read as binary, so convert to str
    print(str(f))
