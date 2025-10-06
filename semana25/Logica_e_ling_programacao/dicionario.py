#1. Dict Comprehension
squares = {x: x**2 for x in range(4)}

#2. Get with Default
d = {'a': 1}
print(d.get('b', 'Not found'))

#3. Merge Dictionaries
d1, d2 = {'a': 1}, {'b': 2}
merged = {**d1, **d2}
print(merged)

#4. Invert Dictionary
d = {'a': 1, 'b': 2}
inv = {v: k for k, v in d.items()}
print(inv)

#5. Count Characters
from collections import Counter
print(Counter('banana'))

#6. Defaultdict for Missing Keys
from collections import defaultdict
d = defaultdict(int)
d['x'] += 1
print(d['x'], d['y'])
 
