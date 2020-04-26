# compute all permutations in a list.

#CODE

import itertools
print(list(itertools.permutations([12,22,23])))

'''
OUTPUT

[(12, 22, 23), (12, 23, 22), (22, 12, 23), (22, 23, 12), (23, 12, 22), (23, 22, 12)]

'''
