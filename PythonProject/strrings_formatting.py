"""Python uses C-style string formatting to create new, formatted strings. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
together with a format string, which contains normal text together with "argument specifiers", 
special symbols like "%s" and "%d".Let's say you have a variable called "name" with your user name in it, 
and you would then like to print(out a greeting to that user.)"""

name = 'Smith'
print('The name is: %s' % name)
print('The name is: {}'.format(name))
print(f'The name is: {name}')

"""To use two or more argument specifiers, use a tuple (parentheses):
%s - strings
%d - integers
%g and %f are for floats """

age = 30
month = 'May'
amount = 500.0
print('The month and age are %s and %d, and the amount is %f' %(month,age,amount))

sal=20.2
name="scoot"
age=20
print("sal is:",sal)
print("name is:",name)
print("age is:",age)
print("name:%s age:%d sal:%g" %(name,age,sal))

"""Any object which is not a string can be formatted using the %s operator as well. 
The string which returns from the "repr" method of that object is formatted as the string. For example:"""

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
print(type(mylist))

"""Here are some basic argument specifiers you should know:
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)"""

"""You will need to write a format string which prints out the data using the following syntax: 
Hello John Doe. Your current balance is $53.44."""

data = ("John", "Doe", 53.44)
format_string = "Hello"

print('%s %s %s. Your current balance is %f' %(format_string,data[0],data[1],data[2]))

# or this way:

data2 = ("John", "Doe", 53.44)
format_string2 = "Hello %s %s. Your current balance is $%s."

print(format_string2 % data2)