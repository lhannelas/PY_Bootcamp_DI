# print ("love")
#
# grid = ["7i3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "^r!" ]
#
# print(grid[3][2])
#
# # print (grid[0][0].isalpha())
# symbol = ["!","#","$","%","^","&","*"]
# print(symbol)
#
# for x in symbol:
#   valid_symbol = x
#   print(valid_symbol)
#
#
# def first_column(x):
#   for el in x:
#       valid = []
#       if el[0].isalpha():
#           valid.append(el[0])
#           print (''.join(valid), end='')
#
#
#
#
#
# def second_column(x):
#   for el in x:
#       valid = []
#       if el[1].isalpha():
#           valid.append(el[1])
#
#       elif el[1] == "%":
#           valid.append(" ")
#
#       print (''.join(valid), end='')
#
#
# def third_column(x):
#   for el in x:
#       valid = []
#       if el[2].isalpha():
#           valid.append(el[2])
#       # elif el[2] == "%" or "#":
#       #     valid.append(" ")
#
#       print (''.join(valid), end='')
#
# first_column(grid)
# second_column(grid)
# third_column(grid)

import re

matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!'
]

decoded = ''

rows_len = len(matrix)
column_len = len(matrix[0])
to_add_space = False

for column_num in range(column_len):
    for row_num in range(rows_len):
        if matrix[row_num][column_num].isalpha():
            decoded += matrix[row_num][column_num]
            to_add_space = True

        elif to_add_space:
            decoded += " "
            to_add_space = False

print(decoded.strip())
