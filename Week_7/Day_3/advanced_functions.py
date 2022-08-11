# print ("hello world")

# numbers = [10, 20, 5]

# print(sum(numbers))

# def out_sum(*args):
#     sum_of_numbers = 0

#     for num in args:
#         sum_of_numbers = sum_of_numbers + num # Its the same like sum_of_numbers += num

#     return sum_of_numbers


# result = out_sum(10, 20, 5, 5, 20)
# print(result)

# def check_keywordedarguments(**kwargs):
#     for key, value in kwargs.items():
#         print(key,":",value)

# check_keywordedarguments(name='sarah', age=24)

# * args ==> Tuple
# **Kwargs ==> dictionnary

# def print_arguments(first_param, second_param,*args, **kwargs):
#     print(f"the first param is {first_param}")
#     print(f"second param is {second_param}")
#     print(f"the input args (Tuple) are: {args}")
#     print(f"the input kwargs (Dictionary) are: {kwargs}")

# print_arguments(10,12,5, 3, age=10)

# valid_input = False

# while not valid_input: # The same as valid_input == False
#     try:
#         num1 = int(input("please enter the first parameter: "))
#         num2 = int(input("please enter the first parameter: "))
#         print(f"the result of the division os {num1 / num2}")
#     except ZeroDivisionError:
#         # this code will be running if we get an exception zero division error
#         print("you cannot divide by zero")
        
#     except ValueError:
#         # this code will be running if we get an exception value error
#         print("please enter a number")

#     else:
#         # This code will run if there is no exceptions
#         valid_input = True

#     finally:
#         #this code will always be running
#         print("all of the code inside the finally will always run")

# print("Good Bye")

# import random

# from time import sleep

# def get_current_temperature():
#     return random.randint(0, 15)

# def main():
#     while True:
#         current_temperature = get_current_temperature()

#         if current_temperature < 5:
#             # create an exception
#             raise Exception(f"the current temperature {current_temperature} is lower than 5")

#         print(f"the current temperature inside the room is {current_temperature}")
#         sleep(2)

# main()


# def upper_string(s):
#     return s.upper()



# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# print(f"fruits before the change {fruit}")

# for i in range(len(fruit)):
#     fruit[i] = upper_string(fruit[i])

# new_fruits = list(map(lambda s: s.upper(), fruit))

# print(f"fruits after the change {new_fruits}")


# def is_starts_with_a(s):
#     return s[0] == "A"


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

# fruits_starts_with_a = []

# for i in range(len(fruit)):
#     if is_starts_with_a(fruit[i]):
#         fruits_starts_with_a.append(fruit[i])

# fruits_starts_with_a = list(filter(is_starts_with_a, fruit))
#fruits_starts_with_a = list(filter(lambda s: s[0], fruit))

# print(f"fruits start with A are: {fruits_starts_with_a}")

from functools import reduce

# def sum_numbers(first, second):
#     return first + second

# numbers = [1, 3, 5, 7]

# sum_of_numbers = 0

# for i in range(len(numbers)):
#     sum_of_numbers = sum_of_numbers + numbers[i]

# sum_of_numbers = reduce(sum_numbers, numbers)
# sum_of_numbers = reduce(lambda first, second : first + second, numbers)

# print(sum_of_numbers)


# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# # def hello(s):
# #     return len(s) <= 4



# say_hello = list(filter(lambda s: len(s) <= 4, people))

# print(say_hello)

# final = list(map(lambda s: f"Hello {s}", say_hello))
# print(final)


def print_parameter(a, b, c):
    print(a)
    print(b)
    print(c)

print_parameter(1, 2, 3)

arguments = [1, 2, 3]
print_parameter(arguments[0], arguments[1], arguments[2])
print_parameter(*arguments) # passing by position

arguments = {
  "a": 1,
  "b": 2,
  "c": 3
}

print_parameter(a=1, b=2, c=3)
print_parameter(**arguments)