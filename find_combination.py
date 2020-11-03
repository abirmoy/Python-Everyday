from itertools import combinations

data = ['a','b', 'c', 'd']

for x in combinations(data, 3):
    print(x)