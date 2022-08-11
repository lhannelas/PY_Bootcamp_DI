import turtle


class Circle:

    def __init__(self, name, radius):
        self.radius = radius
        self.name = name

    def area(self):
        area = self.radius * self.radius * 3.14
        return area

    def draw_a_circle(self):
        return turtle.circle(self.radius)

    def __add__(self, other):
        return self.area() + other.area()

    def __gt__(self, other):
        if self.radius > other.radius:
            return f"{self.name} is the bigger circle"
        elif self.radius < other.radius:
            return f"{other.name} is the bigger circle"

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False


CircleA = Circle("A", 22)
CircleB = Circle("B", 10)

print(CircleA.area())
print(CircleA.draw_a_circle())
CircleC = CircleA + CircleB
print(CircleC)
print(CircleB.area())
print(Circle.__gt__(CircleA, CircleB))



"""
Instructions :
The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle's area
Print the circle and get something nice
Be able to add two circles together
Be able to compare two circles to see which is bigger
Be able to compare two circles and see if there are equal
Be able to put them in a list and sort them
"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = self.compute_area()

    def compute_area(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f'Radius: {self.radius} - Diameter: {self.diameter} - Area: {self.area}'

    def __add__(self, other):
        return f'The two circles have a combined area of {round(self.area + other.area, 2)}'

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __eq__(self, other):
        return self.area == other.area


my_circle = Circle(3)
print(str(my_circle))

my_circle2 = Circle(6)
print(str(my_circle2))

my_circles = my_circle + my_circle2
print(my_circles)

print(my_circle > my_circle2)
print(my_circle < my_circle2)
print(my_circle == my_circle2)

my_list = [my_circle2, my_circle]
sorted_list = sorted(my_list)
list(map(lambda x: print(x), sorted_list))