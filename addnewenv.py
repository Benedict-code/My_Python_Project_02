# Python program to explain os.environ object 
  
# importing os module 
import os
  
# Add a new environment variable 
os.environ['ROBOTBROWSER'] = "C:\\Users\\benedict.ezurike\AppData\Local\Programs\Python\Python310\Scripts\chromedriver\chromedriver.exe"

os.environ['ROBOTBROWSER'] = "C:\\Users\\benedict.ezurike\AppData\Local\Programs\Python\Python310\Scripts\geckodriver\geckodriver.exe"
  
# Get the value of
# Added environment variable 
print("ROBOTBROWSER:", os.environ['ROBOTBROWSER'])