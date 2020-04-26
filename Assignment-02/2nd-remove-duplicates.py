#Write a Python program to remove duplicates from a list of lists.
# code 

import itertools
pg = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", pg)
pg.sort()
new_num = list(pg for pg,_ in itertools.groupby(pg))
print("New List", new_num)

'''
output

Original List [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List [[10, 20], [30, 56, 25], [33], [40]]

'''
