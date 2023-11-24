"""Strings are bits of text. They can be defined as anything between quotes:"""
astring1 = "Hello world!"
astring2 = 'Hello world!'

print("single quotes ' ' ")
print(len(astring2))
# index method 
print(astring1.index('o'))
# count method
print(astring1.count('1'))
#slicing in strings
print(astring1[2:7]) #prints llo w
# leave a colon at the first end:  If you leave out the first number but keep the colon, 
# it will give you a slice from the start to the number you left in. If you leave out the second number, 
# it will give you a slice from the first number to the end.
print(astring1[2:]) #prints llo world!
print(astring1[2:8:]) #prints llo wo
print(astring1[3:7:2]) #This prints the characters of string from 3 to 7 skipping one character. 
#This is extended slice syntax. The general form is [start:stop:step].
print(astring1[1:8:3]) #print eoo
#You can even put negative numbers inside the brackets. 
# They are an easy way of starting at the end of the string instead of the beginning. 
# This way, -3 means "3rd character from the end"
print(astring1[-2]) #print d
print(astring1[-4]) #print r
print(astring1[-2:]) #print d!
print(astring1[-5:])
#There is no function like strrev in C to reverse a string. But with the above mentioned 
# type of slice syntax you can easily reverse a string like this:
print(astring1[::-1]) # prints !dlrow olleH
print(astring1[:-1]) #prints Hello world
#These make a new string with all letters converted to uppercase and lowercase, respectively.
print(astring1.upper())
print(astring1.lower())
#This is used to determine whether the string starts with something or ends with something, 
# respectively. The first one will print True, as the string starts with "Hello". 
# The second one will print False, as the string certainly does not end with "asdfasdfasdf".
print(astring1.startswith('H')) #prints True
print(astring1.endswith('asl')) #prints False
#This splits the string into a bunch of strings grouped together in a list. Since this example 
# splits at a space, the first item in the list will be "Hello", and the second will be "world!".
print(astring1.split(' ')) #prints list ['Hello', 'world!']

#Try to fix the code to print out the correct information by changing the string.
# s = "Hey there! is twenty"
# s = "Hey there! what should this string be?"
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))