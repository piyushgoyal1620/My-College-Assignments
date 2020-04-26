#Write a Python program to extend a list without append.

# code 


x = [10, 20, 30]
y = [40, 50, 60]
y[:0] =x
print(y)

'''
output 

[10, 20, 30, 40, 50, 60]

'''
