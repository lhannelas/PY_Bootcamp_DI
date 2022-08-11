from random import sample


print('ggt')

# Defining a dictionary:
# key-value pair (key: value)
# value can be in Any date type
# keys need to be unique. No duplicate
# Unordered till Python 3.6
# Ordered as from Python 3.7

students_dict = {
    "student1": "Joeri",
    "student2": "Ally",
    "student3": "Shivastav",
    "student4": "Kadeer",
    "student5": "Laurent",
    "student6": "Angkush",
    "student7": "Bruno",
    "ages": [35, 24, 24, 23, 34, 19, 50]   

}

print(students_dict)

# Access the data - using key
print(students_dict['student1'])
print('The first student is {}'.format(students_dict['student1']))

# Access the data - using index
# Keys
keys_students = list(students_dict)
print(keys_students[0])
print(students_dict[keys_students[0]])


# Values
values_students = list(students_dict.values())
print(values_students[0])

# Retrieve age of first student
print (students_dict['ages'][0])

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history = (sample_dict['class']['student']['marks']['history'])
print('History marks:', history)

# Update dictionary
students_dict["student6"] = 'Tooshar'
print(students_dict)

# Add a new entry
students_dict['Instructor'] = 'Damien'
print(students_dict)

# Delete / Remove an entry
del students_dict['student4']
print(students_dict)



# Loop through dictionary
for student in students_dict:
    if students_dict[student] == 'Bruno':
        print('Bruno is present')
        break
    # else:
    #     print(student, students_dict[student])

# Get dictionary of keys, values and items
print(students_dict.keys())
print(students_dict.values())
print(students_dict.items())

# Merget with dictionaries
new_instructor = {'New Instructor': 'Nirmal'}
students_dict.update()

# Using items in for loop
for key, val in students_dict.items():
    print("{} is {}".format(key,val))

#Exercise
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]

print(sample_dict)