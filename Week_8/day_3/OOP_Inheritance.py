class Vehicle:

    def turn_right(self):
        print("turning right")

    def turn_left(self):
        print("turning left")

    def speed(self):
        print("speeding")


class Car(Vehicle):

    def fix(self):
        print("fixing car issues")


class Bus(Vehicle):
    pass


car1 = Car()
car1.speed()


class Animal:
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")


class Bird(Animal):
    pass


rex = Dog("dog", 4, "wouaf")
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs, ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

bird = Bird("bird", 2, "zzz")
print('This animal is a:', bird.type)
# >> This animal is a bird

print('This bird has', bird.number_legs, ' legs')
# >> This bird has 4 legs

print('This bird makes the sound ', bird.sound)
# >> This bird makes the sound zzz
bird.make_sound()
# >> I am an animal, and I love saying zzz

rex.fetch_ball()


class Circle:
    color = "red"


class NewCircle(Circle):
    color = "blue"


nc = NewCircle
print(nc.color)


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor


class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)


nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)


class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Dog(Animal):
    def __init__(self, is_lazy, type, number_legs, sound):
        super().__init__(type, number_legs, sound)
        self.is_lazy = is_lazy

    def fetch_ball(self):
        if self.is_lazy:
            print("I dont want to fetch the ball")
        else:
            print("I am a dog, and I love fetching balls")

    def make_sound(self):
        super().make_sound()
        print("I am an DOGGG !!! WOUAFFF!!")


rex = Dog(False, 'dog', 4, "Wouaf")
rex.fetch_ball()


# rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!


class Door:
    def __init__(self, is_opened):
        self.open = is_opened

    def open_door(self):
        print("The door is open")

    def close_door(self):
        print("The door is closed")


class BlockedDoor(Door):
    def open_door(self):
        raise Exception("Error! The door is blocked")

    def close_door(self):
        raise Exception("Error! The door is blocked")


door = BlockedDoor(False)

door.open_door()
door.close_door()


