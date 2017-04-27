# Lesson 4
# csv, or "comma separated value" files are nice for us because they appear familiar with excel users
import csv

with open('mydata.csv', 'w') as f:
    w = csv.writer(f, delimiter=',', lineterminator='\n')
    w.writerow([1, 2, 3, 4, 5])
    w.writerow([1, 2, 3, 4, 5])

with open('mydata.csv', 'r') as f:
    r = csv.reader(f, delimiter=',', lineterminator='\n')
    for row in r:
        print(row)
