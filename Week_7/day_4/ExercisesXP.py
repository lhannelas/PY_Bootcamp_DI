# Exercise 1
# import random
#
# print('Hello World!')
#
# winter = range(-10, 16)
# summer = range(16, 40)
#
#
# def get_random_temp(season):
#     if season == winter:
#         value = round(random.uniform(-10, 16), 1)
#         return value
#     elif season == summer:
#         value = round(random.uniform(16, 40), 1)
#         return value
#
#
# def main():
#     ans = int(input('What month is it? i.e 1 = January, 12 = December  : '))
#     if ans in range(1, 4) or ans in range(10, 12):
#         temperature = get_random_temp(summer)
#         print(f'The temperature right now is {temperature} degrees Celsius.')
#
#         if 16 <= temperature < 23:
#             print("Put a light pullover, it is not warm yet")
#         elif 24 <= temperature < 32:
#             print("Weather is nice, enjoy")
#         else:
#             print("Its damn hot, let's go to the beach")
#
#     elif ans in range(5, 8):
#         temperature = get_random_temp(winter)
#         print(f'The temperature right now is {temperature} degrees Celsius.')
#         if temperature < 0:
#             print("Brr, that's freezing! Wear some extra layers today")
#         elif 0 <= temperature < 16:
#             print("Quite chilly! Don't forget your coat")
#
#
# main()


# Exercise 2

def get_age(year, month, day):
    current_day = 18
    current_month = 7
    current_year = 2022

    if current_month < month:
        actual_month = current_month
        actual_year = (current_year - 1) - year
    else:
        actual_month = current_month - month
        actual_year = current_year - year

    if current_day > day:
        actual_day = current_day - day
    else:
        actual_day = 30 - (day - current_day)


    print(f'You are is {actual_year} years, {actual_month} months and {actual_day} days old')


get_age(1951, 10, 23)
