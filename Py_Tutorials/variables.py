#Variables are containers that store data.
can=("soda")
print(can)
can="beans"
print(can)
#Type of variables
print(type(can))
#Bill
pizza=100
samosa=20.5
ice_cream=100
total=pizza+samosa+ice_cream
print(total)
print(type(total))
#Boolean
above_threshold=total > 200
print(above_threshold)
#In Python everything is an object, no need to define the type of variable to use it.
#id() function is used to get the memory address of an object
print(id(above_threshold))
#Rules to define a variable name
#1. A variable name must start with a letter or the underscore character
#2. A variable name cannot start with a number
#3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#4. Variable names are case-sensitive (age, Age and AGE are three different variables)
#5. The variable name should not be a reserved keyword (true, def, if, else, etc.)
#6. Variable name should be descriptive
#7. Variable name should be short and meaningful
#8. Variable name should not start with double underscore
