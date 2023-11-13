
# import ldap
# import sys
# import time
# import datetime

# from calendar import monthrange
# from random import randint

##Check Chrome is installed
# from selenium import webdriver
# driver = webdriver.Chrome()

# from datetime import datetime, timedelta

# def GenerateFutureDate():   
#     dt = datetime.now()
#     td = timedelta(days=4)
# # your calculated date
# #my_date = dt + td
# print(dt+td)

# def Generate_Future_Date(days):
#     """Library for generating future date 

#     Examples:
#         | Generate Future Date | 14 |
#     """

#     #return "%s" % (datetime.datetime.strftime((datetime.datetime.today() + datetime.timedelta(int(days))),'%m-%d-%Y'))

#     #return "%s" % (datetime.datetime.strftime((datetime.datetime.today() + datetime.timedelta(int(days))),'%m-%d-%Y')) 

#     return datetime.datetime.now()

# x=Generate_Future_Date(1)
# print(x.strftime("%A"))

###19/9
##Randon Number Generation
# import random

# print(random.randrange(1,10))

##Type casting
# x = int(2)
# y = int(5.5)
# z = int("4")
# print(x,y,z)
# x = float(7)
# y = float(9.9)
# z = float("7")
# print(x,y,z)
# x = str(3)
# y = str(6.6)
# z = str("8")
# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))

##Multiline strings
# s = """""This is a multiline strings
# and it extends to about 
# three lines"""""
# print(s)
# print(type(s))

# for x in "banana":
#     print(x)

##formatting
# age=40
# # txt="My name is Harry, I am {}"
# # print(txt.format(age))
# txt= "My name is Tan, I am %g"
# print(txt % age)