# class School:
#     name = "schoolA"
#     num_of_students = 200
#     num_of_classes = 10

from itertools import groupby


class Car:

    def __init__(self, color, type, brand):
        print("at the init function")
        self.color = color
        self.type = type
        self.brand = brand

    def turn_right(self):
        print(f"turning right the car of type {self.type}")

    def speed(self):
        print("speeding")

    def slow(self):
        print("slowing down")

    def turn_left(self):
        print("turning left")


car1 = Car("Red", "Ford", "Mustang")
car2 = Car("Blue", "Toyota", "Prius")

car1.turn_right()
Car.turn_right(car1)

car2.turn_right()
Car.turn_right(car2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# create an instance of the class
p = Point(3, 4)

# access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)


class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))


shelter_dog = Dog("Rex")
shelter_dog.walk(10)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)


first_person = Person("John", 36)
second_person = Person("Laurent", 34)

first_person.show_details()
second_person.show_details()


class Computer:

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        # Analyse the line below
        print(self)


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


laurent_fund = BankAccount("00013320033", 5000)

laurent_fund.view_balance()
laurent_fund.deposit(500)
laurent_fund.withdraw(200)
laurent_fund.withdraw(10000)
laurent_fund.view_transactions()

BankAccount.view_balance(laurent_fund)


# Daily Challenge
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def get_animal_types(self):
        animal_list = list(self.animals.keys())
        animal_list.sort()
        return animal_list

    def get_short_info(self):
        x = self.get_animal_types()
        info = f"McDonald's farm has {', '.join(x)}."
        print(info)

    def add_animal(self, name, mount=1):
        if name in self.animals:
            self.animals[name] += mount  # self.animals[name] = self.animals[name] + mount
        else:
            self.animals[name] = mount

    def get_info(self):
        result = f"""{self.name}'s farm

"""

        # for key, value in self.animals.items():

        for key in self.animals:
            result += f"{key}: {self.animals[key]}\n"

        result += "\tE-I-E-I-0!"
        return result


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()


# ExerciseXP
# Exercise 1


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


first_cat = Cat("Diego", 3)
second_cat = Cat("Aya", 4)
third_cat = Cat("Luna", 2)


def oldest_cat(*args):
    return max(args)


print(
    f"The oldest cat is {second_cat.name}, and is {oldest_cat(first_cat.age, second_cat.age, third_cat.age)} years old.")


# Exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        return f"{self.name} goes woof!"

    def jump(self):
        x = self.height * 2
        return f"{self.name} jumps {x}cm high!"


davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
print(davids_dog.bark())
print(davids_dog.jump())

sarahs_dog = Dog("TeaCup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
print(sarahs_dog.bark())
print(sarahs_dog.jump())

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)


# Exercise 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("\n".join(self.lyrics))


stairway = Song(["There's a lady who's sure", "all that glitter is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("animal already on the list")
        else:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("There is no such animal in the Zoo")

    def sort_animals(self):

        util_func = lambda x: x[0]
        temp = sorted(self.animals, key=util_func)
        res = [list(ele) for i, ele in groupby(temp, util_func)]
        print(res)


laurent_zoo = Zoo("Lorito")
laurent_zoo.add_animal("Giraffe")
laurent_zoo.get_animals()
laurent_zoo.add_animal("Lion")
laurent_zoo.add_animal("Elephant")
laurent_zoo.add_animal("Elephant")
laurent_zoo.add_animal("Tiger")
laurent_zoo.add_animal("Monkey")
laurent_zoo.add_animal("Lemurian")
laurent_zoo.add_animal("Cat")
laurent_zoo.add_animal("Dog")
laurent_zoo.add_animal("Bird")
laurent_zoo.add_animal("Bluebird")
laurent_zoo.add_animal("Bear")
laurent_zoo.get_animals()
laurent_zoo.sell_animal("cat")
laurent_zoo.sell_animal("Tiger")
laurent_zoo.get_animals()
laurent_zoo.sort_animals()

