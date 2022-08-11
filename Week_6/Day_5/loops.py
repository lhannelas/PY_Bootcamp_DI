# print("Loops")

# students = [
#   'Joeri',
#   'Ally',
#   'Shivastav',
#   'Kadeer',
#   'Laurent',
#   'Angkush',
#   'Bruno'
# ]
# # For Loops
# for student in students:
#     print(student)

# # From 0 to 4
# for i in range(5):
#     print(i)

# # From 1 to 5
# for i in range(1,6):
#     print(i)

# # Iterate through the string
# for elem in 'string':
#     print(elem)

# # Iterate through a tuple
# for item in ('one', 'two', 'three'):
#     print(item)


# # exercise
# # number = input ('PLease enter a number')
# #Need to try again
# # for i in range(0,13):
# #   print (str(i)+ '*' + i)
# #   print = int(number) * i 
  
# # While loop
# # while (True) => It will run continuously (infinite loop -be careful)

# # expression = True # 1 , 'string'
# # while (expression):
# #   print("This is an infinite loop")

# flag = True
# while flag:
#     num = input('PLease enter a positive number:')
    
#     if int(num) > 0:
#         flag = False
#         print("Congratulations!")
#     else:
#         print("Number is not positive")

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # Break Statement
# while True:

#     num = input('PLease enter a positive number:')
    
#     if int(num) > 0:
#         break
        
#     else:
#         print("Number is not positive")

# print("Congratulations")

# Continue Statement
# count = 0
# while count < 11:
#     if count == 3:
#         count += 1
#         continue
#     else: 
#         print(count)

   

# print('Finished')

# Advanced Loops
# For Loop with steps
# range(Start, Stop, Step)
from ast import Break


for num in range(1, 20, 3): 
  print(num)

print(list(range(1,20,2)))

alphabet = "abcdefgh"
for a in alphabet:
    print(a)

for idx in range(len(alphabet)):
  print(idx, alphabet[idx])

for item in enumerate(alphabet):
  print(item) #tuple (index, value)

for idx, val in enumerate(alphabet):
    print(idx, val)
    print('At index {} the value is {}'.format(idx, val))

# zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

for item in zip(list1, list2, list3):
    print(item)  # returns a tuple containing the item at the same index from all the list

# For-Else
# Else is optional - executed once after the for loop (exept if break statement is executed)

for num in range(1, 20, 3): 
    print(num)
    if num == 10:
        break
else:
    print('All odd numbers generated') # Executed only if break not encountered
print('For-loop completed')

# While-Else
x = 0
while x < 10:
    print(x)
    x += 1
    if x == 5:
        break
else:
    print ('x is not smaller than 10. x is ' + str(x)) # Executed only if break not encountered


print('while loop completed')


print('odd numbers generated')


for num in list1:
    # retrieve data from databse
    pass

