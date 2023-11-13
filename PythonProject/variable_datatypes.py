""" To define a floating point number, you need to input"""
myfloat = 5.0
print(myfloat)
"""or define by casting"""
myfloat = float(3)
print(myfloat)

"""strings can be define either by using double quotations or single quotations"""
mystrings = "explanation"
print(mystrings)
mystrings = 'example'
print(mystrings)

"""concatenate strings"""
a = "welcome"
b = "abored"
print(a + " " + b)

""" exercise"""
mystring = "hello"
myfloat = 10.0
myint = 20
print(mystring,myfloat,myint)
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
    print("String: {}" .format(mystring))
    print(f'String: {mystring}')
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
    print("Float: {}".format(myfloat))
    print(f'Float: {myfloat}')
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    print("Int: %d" % myint)
    print("Int: {}".format(myint))
    print(f'Int: {myint}')
