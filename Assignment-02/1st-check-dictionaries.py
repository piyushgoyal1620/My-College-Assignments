#Write a Python program to check if all dictionaries in a list are empty or not.

#code 

Piyush = [{},{},{}]
Goyal = [{4,5},{},{}]
print(all(not f for f in Piyush))
print(all(not f for f in Goyal))

'''
output

True
False

'''
