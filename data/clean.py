import sys

file = sys.argv[1]

o = open(file)
data = o.read().lower()
o.close()

data = [elem.strip() for elem in data.split('\n')]
data = filter(None, data)
data.sort()

for elem in data:
    print elem
