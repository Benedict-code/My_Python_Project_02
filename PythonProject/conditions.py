"""Python uses boolean logic to evaluate conditions. The boolean values True and False 
are returned when an expression is compared or evaluated. For example:"""
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#Notice that variable assignment is done using a single equals operator "=", whereas 
# comparison between two variables is done using the double equals operator "==". 
# The "not equals" operator is marked as "!="

"""Boolean operators
The "and" and "or" boolean operators allow building complex boolean expressions, for example:"""
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

""" The 'in' operator """
#The "in" operator could be used to check if a specified object exists within an 
# iterable object container, such as a list:
name == "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

"""Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, 
although tabs and any other space size will work, as long as it is consistent. 
Notice that code blocks do not need any termination.
Here is an example for using Python's "if" statement using code blocks:"""
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something
    pass
else:
    # do something
    pass

x = 2
if x == 2:
    print("x equals two")
else:
    print("x does not equal to two.")

""" A python statement is evaluated as True if one of the following is correct: 
1. The 'True' boolean variable is given, or calculated using an expression, such as an arithemtic comparison.
2. An object which is not considered 'empty' is passed.
Examples of python objects which are considered as empty:
1. An empty string ''
2. An empty list []
3. The number zero
4. The false boolean variable: False"""

""" The 'is' operator"""
"""Unlike the double equals operator '==', the 'is' operator does not match the values of the variables,
but rather, the instances themselves. Example:"""
x = [1,2,3]
y = [1,2,3]
print(x == y) # prints out True
print(x is y) # prints out False

""" The 'not' operator"""
""" Using 'not' operator before a boolean expression inverts it:"""
print('Next page')
print(not False) # prints out True
print(not True) # prints out False
print((not False) == (False)) # prints out False
print((not False) == (True)) # prints out True
print('Next page')

""" Exercises"""
""" Change the variables in the first section, so that each if statement resolves as True"""
# change this code
number = 20
second_number = 0     # [], False, ''
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")