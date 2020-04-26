#Write a Python program to iterate over two lists simultaneously.

# code

Piyush = [1, 2, 3]
color = ['Piyush', 'Goyal', 'Coder']
for (a,b) in zip(Piyush, color):
    print(a, b)

'''
OUTPUT

1 Piyush
2 Goyal
3 Coder

'''
