"""basic mathematical operators can be perform in python with numbers
. Does pyhton follows concept of BODMAS? """

number = 1 + 2 * 3 / 4.0
print(number)

"""Another operator available is the modulo (%) operator, which returns the 
integer remainder of the division. dividend % divisor = remainder."""

remainder = 11 % 3
print(remainder)

""" Using two multiplication symbols makes a power relationship. """
sqaured = 7 ** 2
cubed = 2 ** 3
print(sqaured)
print(cubed)

""" we can also use addition operator in strings for concatenation, 
Python supports concatenating strings using the addition operator:"""
val1 = 'hello'
val2 = 'world!'
print(val1 + " " + val2)

"""
Python also supports multiplying strings to form a string with a repeating sequence:"""
lotsodhello = "hello" * 10
print(lotsodhello)

"""Lists can be joined with the addition operators:"""
mylist1 = []
mylist2 = [1,2,3,4]
mylist3 = ['orange','mango','banana']
alllists = mylist1 + mylist2 + mylist3
print(alllists)

"""Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:"""
repeatedlists = [1,2,3]
print(repeatedlists * 2)

"""The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the 
variables x and y, respectively. You are also required to create a list called big_list, 
which contains the variables x and y, 10 times each, by concatenating the two lists you have created."""

x = 3
y = 5
x_list = [x * 10]
y_list = [y * 10]
big_list = [x * 10, y * 10]

print(x_list)
print(y_list)
print(big_list)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")






