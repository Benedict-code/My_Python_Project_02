
# print("Hello, Word!")

# month = "Jun"
# print(type(month))


import datetime

######The datetime module has many methods to return information about the date object.

# x = datetime.datetime.now()
# #print(x)
# print(x.year)
# print(x.strftime("%A"))

# the datetime is called by the object datetime
# x = datetime.datetime(2023, 5, 20)
# print(x)

###datetime object has a method for fromatting date objects into readable strings, this is called "strftime()" and takes one parameter "format" to specify
### specify the format of the returned string.

# x = datetime.datetime(2020, 6, 29)
# print(x.strftime("%B"))

# #todays date
# x = datetime.datetime.today()
# print(x)

# #today
# x = datetime.timedelta(5)
# print(x)

# # concatnate
# x = datetime.datetime.strftime(datetime.datetime(2021, 10, 30) + datetime.timedelta(1), '%Y-%m-%d')
# y = datetime.datetime.strftime(datetime.datetime(2021, 10, 30) + datetime.timedelta(1), '%Y %m %d')
# print(x,y)

#python modules "Python has wide range of modules and are usable as when needed, it also contains wide variety of methods"
# we can create a module with file extension .py
# module can be imported as an alias: 
# import mymodule as mx 
# mx.get()

# dir() function is a build-in function which list all the function name(or variable names) in a module. it can be used on all modules E.G:
# import platform as pt
# import pprint
# import json
# x= dir(pt)
# # print(dir(pprint))
# # print(dir(datetime))
# print(x)

