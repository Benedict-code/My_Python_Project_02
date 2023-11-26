""" Pyhton Loops"""
""" There are two types of loops in python:
1. FOR
2. WHILE
"""
""" The 'for' loop"""
""" For loops iterate over a given sequence. Example:"""
numbers = [2, 3, 4, 5, 6]
for number in numbers:
    print(number)

""" For loops can also iterate over a given sequence of numbers using the 'range' and 'xrange' functions.
The difference between range and xrange is that the range function returns a new list with numbers of that specified range, 
whereas xrange returns an iterator, which is more efficient. Pyhton 3 uses the range functiion, which acts like xrange. 
Note that the range function is zero based."""

print('Next page')
for x in range(5):
    print(x) # Prints our the numbers 0,1,2,3,4
print('Next')
for x in range(3, 6):
    print(x) # prints out 3,4,5
print('Next')
for x in range(3, 8, 2):
    print(x) #prints out 3,5,7