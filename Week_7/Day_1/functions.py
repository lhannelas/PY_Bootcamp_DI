# Defining a function
import functools


def name_of_the_function():
    """ Docstrings - Provide some info about the function"""
    print("Hello World!")
    print("Happy to see")


# Calling a function
name_of_the_function()

# Passing information to a function

def say_hello(name):  # Parameter => variable
    print("Hello {}".format(name))

say_hello('Laurent')  # Argument => value i.e Laurent

students = [
  'Joeri',
  'Ally',
  'Shivastav',
  'Kadeer',
  'Laurent',
  'Angkush',
  'Bruno'
]

for student in students:
    say_hello(student)

# Two or more parameters/arguments (Try not to use more than 5 parameters)
def find_sum(a, b):
    print('{}'.format(a+b))


find_sum(1, 2)
find_sum(2, 3)

# Default values
#find_sum(1)

def find_sum_default(a=None, b=None):
    if a is None:
        print('both arguments misssing')
    elif b is None:
        print('Second argument missing')
    else:
        print('{}'.format(a+b))


find_sum_default()
find_sum_default(1)
find_sum_default(1,2)


def say_hello_lang(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)


say_hello_lang("Rick", "FR")
say_hello_lang("Bruno", "EN")
say_hello_lang("Francesco", "IT")

# Keyword Arguments (name-value pair)
say_hello_lang("FR", "Rick")
say_hello_lang(language="FR", username="Rick")

# Always specify keyword arguments AFTER positional arguments
say_hello_lang("Rick", language="FR")


# Global Scope
day = 'Monday' # Global variable

def get_today_temp(temp):
    print("Today is {} and it is {}C".format(day, temp))


get_today_temp(18)
#print(temp) # temp is defined only within the function - local scope


# Return a value
def find_sum_return(a, b):
    print('{}'.format(a + b))
    return a + b

sum = find_sum_return(1, 3)
print("Sum is {}".format(sum))

# Returning more than one value
def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

firtname, lastname = format_name('damien', 'maLlet')
print("Name is {} {}".format(firtname, lastname))


def calculation(a,b):
    return (a + b , a - b)
    

res = calculation (40, 10)
print(res)


# List as an argument
def greet_persons(persons):
    for person in persons:
        print('Hello {}'.format(person.title()))

greet_persons(students) #takes student list from the beginning

# lambda functions
# A squaring lambda function
# A squaring lambda function
square = lambda n : n*n
num = square(5)
print (num)

# A substraction lambda function
# A subtraction and addition lambda function with multiple arguments
sub = lambda x, y : x-y
print(sub(5, 3))

add = lambda a, b : a+b
print(add(5, 3))


# MApping using lambda function
myList = [10, 25, 17, 9, 30, -5]
# Double the value of each element
myList2 = map(lambda n : n*2, myList) # return an object
print(myList2) # Address of the object
print (list(myList2))

# Filtering using lambda
myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
myList3 = filter(lambda n : n%5 == 0, myList)
print (list(myList3))


# Exercise
# Find the standard deviation of a list of values
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#workout the mean
def  find_mean(nums):
      return sum(nums)/len(nums)

u = find_mean(values)
# Then for each number subtract the mean and square the result

diff = list(map(lambda n : (n-u)*(n-u), values))
print (diff)

#Then workout the mean of those squared differences
var = find_mean(diff)
print (var)

# Take the square root of that and wwe are done!
import math
stddev = math.sqrt(var)
print('{:.3f}'.format(stddev))

import statistics
print('{:.3f}'.format(statistics.pstdev(values)))


# SETS
student_set = set()
student_set.add('Bruno')
student_set.add('Angkush')
student_set.add('Shivastav')
student_set.add('Laurent')

print(student_set)

student_set.add('Bruno')
print(student_set)

py_pt_43 = {'Bruno', 'Angkush', 'Shivastav', 'Laurent', 'Ally', 'Kadeer', 'Yuri'}
print(py_pt_43)


