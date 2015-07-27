import sys
from collections import Counter

file = open(sys.argv[1])
skills = Counter(file.read().split('\n'))
file.close()

for skill in skills.most_common():
    print skill

