'''
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''


#CODE

for i in range (1,6):
    for j in range(i):
        print("*", end=' ')
    print("\r")
for i in range (5, 1, -1):
    for j in range(0, i-1):
        print("*", end=' ')
    print("\r")

'''
OUTPUT : 

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''
