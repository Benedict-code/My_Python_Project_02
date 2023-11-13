# Python program to explain os.environ object 

# importing os module 
import os
import pprint

# Get the value of
# 'HOME' environment variable
# BROWSER = os.environ['ROBOTBROWSER']

# # Print the value of
# # 'HOME' environment variable
# print("ROBOTBROWSER:", BROWSER)

# # Get the value of
# # 'JAVA_HOME' environment variable
# # using get operation of dictionary
# java_home = os.environ.get('JAVA_HOME')

# # Print the value of
# # 'JAVA_HOME' environment variable
# print("JAVA_HOME:", java_home)

# os.environ["MYVARIABLE"]    =   "3"
# print(os.environ["MYVARIABLE"])

# #ADD
# os.environ["ROBOT_PASSWORD"] = 'SoftwareTesting070$'
# print("ROBOT_PASSWORD:", os.environ["ROBOT_PASSWORD"])

#Access
robot_password = os.environ["ROBOT_PASSWORD"]
print("ROBOT_PASSWORD:", robot_password)

defaultpassword = os.environ["DEFAULTPASSWORD"]
print("DEFAULTPASSWORD:", defaultpassword)

# #Get the lists of users environment variables
# env_var = os.environ
# #Print the lists of user's envirorment varibales
# print("User's Environment Variables")
# pprint.pprint(dict(env_var), width = 1)

# #Accessing a particular envirorment varibles
# java_home = os.environ['JAVA_HOME']
# #Print the value of "HOME" environment variable
# print("JAVA_HOME:", java_home)

# robot_password = os.environ["ROBOT_PASSWORD"]
# print("ROBOT_PASSWORD:", robot_password)

# lang = os.environ["LANG"]
# print("LANG:", lang)

# #Modifying environment variables:
# #print APPDATA enviroement variable
# print("APPDATA:", os.environ["APPDATA"])
# # #modify the value
# # os.environ["APPDATA"] = ''
# #print modified APPDATA
# # print("Modified APPDATA", os.environ["APPDATA"])

# #Adding a new environment variables
# os.environ["GeeksForGeeks"] = 'www.geeksforgeeks.org'
# print("GeeksForGeeks:", os.environ["GeeksForGeeks"])


# #Accessing environment variables which does not exist
# print("MY_HOME:", os.environ["MY_HOME"])

#Handling error while accessing a environment varible which does not exist
# #Method 1
# print("MY_HOME:", os.environ.get('MY_HOME', 'Environment variable does not exist'))
#Method 2
# try:
#     print("MY_HOME:", os.environ["MY_HOME"])
# except:
#     print("Environment varibale does not exist")
