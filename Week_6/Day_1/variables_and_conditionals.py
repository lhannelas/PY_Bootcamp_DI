# print('variables and conditionals')

# #delaring a variable
# name1 = 'Laurent'
# print(name1)
# print('My name is ' + name1 + ' and I am currently doing my first Hackhathon.')
# print('My name is {} and I am currently doing my first Hackhathon.'.format(name1))
# print(f'My name is {name1} and I am currently doing my first Hackhathon.')

# age = 34

# # string formatting and variable display
# print('My name is ' + name1 + ' and my age is ' + str(age))
# print('My name is {} and my age is {}'.format(name1, age))
# print(f'My name is {name1} and my age is {age}')
# print('My name is', name1, 'and my age is', age)


# # Increment a value
# num = 0
# print(num)

# num = num + 1
# print (num)

# num += 1
# print (num) 


# # Take user input
# name = input('Please state your name: ')
# print('My name is ' + name)

# age = input('Please enter your age: ')
# print(f'My name is {name} and my age is {age}')

# new_age = int(age) + 5

# print('My name is ' + name + ' and my age is ' + str(new_age))
# print(f'My name is {name} and my age is {new_age}')

# #exercise
# age = input("How old are you? ")
# print("You are {} years old".format(age))

# # conditionals
# # if <condition> : condition: evaluating whether it is true or false
# #    code          code: important to be indented (for multiple lines), 
# #                        will run if condition is True

# if int(age) > 18:
#   print("You are an adult")
# print("Congratulation") # This line will be executed irrespective of the if statement (not indented)

# # if-else statement and elif (equivalent of else if)
# if int(age) > 60:
#     print("You can travel for free in Mauritius!")
# elif int(age) == 60:
#     print("Congratulations on being able to travel for free now in Mauritius!")
# elif int(age) == 59:
#     print("Next year you will be able to travel for free in Mauritius")
# else:
#     print("Sorry, you need to pay to travel!")

# print('Finished')

# # Multiple / combined comparisons 
# a = 1
# b = 2
# c = 0

# if a < b and not c > a: # and : both conditions need to be True, not: opposite of boolean (True/False)
#     print('Both condition are met')
   
# elif a < b or c > a: # if at least one condition is True
#     print('Only one condition is met')
# else:
#     print('Conditions not met')

# # In 
# vowels = "aeiouy" # string is a sequence of characters
# vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
# letter = 'a'
# print(letter in vowels)
# print('b' in vowels)
# print('c' in vowels)
# print('d' in vowels)
# print('e' in vowels)

# hobbies = ["TV", "eating", "coding", "gaming"]
# student_hobby = "coding"
# if student_hobby in hobbies:
#     print("Welcome to the club")


# Sequences - category of data types (List, Tuple, String)
# Lists - vrsatile sequence type 

from sqlite3 import complete_statement


vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
print(vowels_list)

vowels_list = [1 , 2 , 3 , 4 , 5]
print(vowels_list)

# Tuple - Like a list, BUT they are immutable ( they cannot be changed)
vowels_tuple = ('a', 'e', 'i', 'o', 'u', 'y')
print(vowels_tuple)

# Strings - special sequence that can only contain characters
vowels_str = 'aeiouy'
print(vowels_str)

# Indexing in sequence
# starts with zero
print(vowels_list[0])
print(vowels_tuple[0])
print(vowels_str[0])

# last element
print(vowels_list[len(vowels_list)-1])
print(vowels_list[-1])
print(vowels_tuple[-1])
print(vowels_str[-1])

# range of elements
print(vowels_list[0:3])  # start:end (but does not include value at end index)
print(vowels_tuple[:3])  # if start index is not specified, default 0
print(vowels_str[0:3])

print(vowels_list[3:])   # if end index not specified, default last index
print(vowels_tuple[3:])
print(vowels_str[3:])


# List Methods
# Update element
vowels_list[0] = 'b'
print(vowels_list)

#vowels_list[10] = 'z' #this will result in index error . That index does not exist
#print(vowels_list)

# Add a new element
vowels_list.append('z')
print(vowels_list)

# Remove an element
vowels_list.remove('b')
vowels_list.remove('z')
print(vowels_list)

# Adding two list
missing_vowel = ['a']
complete_vowels = missing_vowel + vowels_list  #combining lists
print(complete_vowels)

# sorting
unsorted_char = [ 'b', 'm', 'e', 's', 'a']
unsorted_nums = [2, 1, -3, 8, -10]
print(sorted(unsorted_char))
print(sorted(unsorted_nums))

# length
print(len(unsorted_nums))

# sum
print(sum(unsorted_nums))

print('Average of unsorted_nums:', sum(unsorted_nums)/len(unsorted_nums))


# More Methods
food = ['spam', 'eggs', 'ham']
food.append('sushi')
print(food)
# ['spam', 'eggs', 'ham', 'sushi']

food.insert(0, 'beans')
print(food)
# ['beans', 'spam', 'eggs', 'ham', 'sushi']

food.extend(['bread', 'water'])
print(food)
# ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']

# Tuple
my_tuple =(1, 2 ,3, [4, 5], "6")
print(my_tuple)
print(my_tuple[0])

# Attempt to change the first element
# my_tuple[0] = 9
# TypeError

print(my_tuple[3][0])
# Item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple)
