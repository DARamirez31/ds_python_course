#To store strings you can use single quotes or double quotes
first="Mohan"
last='Kumar'
name=first+" "+last
print(name)
#python format strings using f-string
age = 27
info = f"{first} {last} is {age} years old"
print(info)
#index of the string starts from 0
print(name[0])
print(name[0:5]) #slicing does not include the last index
print(name[-1]) #last character
print(name[0:-1]) #all characters except the last one
print(name[6:])  #all characters from 6th index
print(name[:6])  #all characters till 6th index
print(name[0:6:2]) #every 2nd character from 0 to 6
print(name[::-1]) #reverse the string
print(name[2:len(name)]) #slicing from 2nd index to the end
#strings are immutable, meaning you cannot change the value of a string once it is created
#name[0]="N" #this will throw an error

#use single quotes inside double quotes and vice versa
print("He said, 'I am coming'")
print('He said, "I am coming"')
#multiline string
print('''This is a multiline string
that spans multiple lines''') #use triple quotes

#String methods
#capitalize() - converts the first character to upper case
print(name.capitalize())
#casefold() - converts string into lower case
print(name.casefold())
#center(width) - returns a centered string
print(name.center(20))
#count() - returns the number of times a specified value occurs in a string
print(name.count("a"))
#encode() - returns an encoded version of the string
print(name.encode())
#endswith() - returns true if the string ends with the specified value
print(name.endswith("r"))
#expandtabs() - sets the tab size of the string
print(name.expandtabs(2))
#find() - searches the string for a specified value and returns the position of where it was found
print(name.find("Kumar"))
#format() - formats specified values in a string
print("My name is {0}".format(name))
#format_map() - formats specified values in a string
print("My name is {name}".format_map({'name':name}))
#index() - searches the string for a specified value and returns the position of where it was found
print(name.index("Kumar"))
#isalnum() - returns True if all characters in the string are alphanumeric
print(name.isalnum())
#isalpha() - returns True if all characters in the string are in the alphabet
print(name.isalpha())
#in() - returns True if a sequence with the specified value is present in the string
print("Kumar" in name)

print(dir(str))

#replace() - replaces a specified value with another specified value
s="patient was charged 100$ for lab test"
print(dir(s))
s=s.replace("100$","200$")
print(s)
#upper() - converts a string into upper case
print(s.upper())
#lower() - converts a string into lower case
print(s.lower())
#title() - converts the first character of each word to upper case
print(s.title())
#isdigit() - returns True if all characters in the string are digits
print(s.isdigit())
print('4de'.isdigit())
#index() - searches the string for a specified value and returns the position of where it was found
print(s.index("lab"))

#can't join strings and numbers
#s="The patient was charged "+100+"$ for lab test"
print(s)
#use str() function to convert numbers to string
s="The patient was charged "+str(100)+"$ for lab test"
print(s)

#tab character
a="hello\tworld"
print(a)

#split() - splits the string into substrings if it finds instances of the separator
print(s.split(" "))
print(s.split(" ",maxsplit=2))

#strip() - removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
s="   patient was charged 100$ for lab test   "
print(s)
print(s.strip())

#endwith() - returns True if the string ends with the specified value
file_name='data.csv'
print(file_name.endswith('.csv'))






