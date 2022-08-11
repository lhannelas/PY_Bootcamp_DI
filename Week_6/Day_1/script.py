from re import T


print ("this is my first python scriptd")
print(type(1)) # int
print(type('1')) # str
print(type(False)) # boolean
print(type('false')) #str
print (type(1.25)) # float

# Strings
print("Hello, world!")
print('Hello, world!')

# String in-built functions (methods)
print('hello, world'.capitalize())
print('hello, world'.lower())
print('hello, world'.upper())
print('hello, world'.replace('hello', 'hi'))
print('hello, world'.index('h'))
print('hello, world'.startswith('hello'))

# Numbers- Integers (int-whole numbers) and Floats (float-point numbers)
print(type(1))   # int
print(type(1.0)) # float

# Arithmetic operations
print(3+4)  #addtion
print(3-4)  #subtraction
print(3*4)  #multiplication
print(4/3)  # division
print(4//3) #Floor division
print(4%3) # Remainder (Modulus) of (4/3)

# Type Casting - Convert a type to another
print('12' + str(2)) # concatenate strings
print(int('12') + 2) # addtion
# We can only add value of the same type (str+str or number + number)
# We cannot add string and number

# Special Characters
print("Today is Monday. \nThis evening is quite chilly.") #new line

print("Group \t\tStudent 1 \tStudent 2")  #tab
print("Cool as Code \tJoeri \t\tBruno")
print("WestTech \tLaurent \tAngkush")
print("FunRunGame \tAlly \t\tShivastav")

# Booleans - True or False
print(True)
print(False)
# Does not exist
#print(true) # Does not exist
#print(false)
# Equivalebt in Numbers
print(int(True))  # 1
print(int(False)) # 0
print(str(True))  # 'True'
print(str(False)) # 'False'

print('HELLO'.isupper()) # True
print(3<2)               # False

# Comparisons
# <     - Less than
# >     - Greater than
# ==    - Equal to
# !=    - Not equal to
# <=    - Less than or equal
# >=    - Greater than or equal

# Booleean functions
print(6 == 6)
print(6 is 6)
print(6 is not 5)   # 6 != 5
print(bool(5))
print(bool(0))
print(bool(-2))
print(bool('hello'))
