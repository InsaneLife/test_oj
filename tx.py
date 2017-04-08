
str = raw_input()
print str


import sys
for line in sys.stdin:
    for value in line.split():
        print(value)