class Person:
    def __init__(self, name):
        self.name = name
        self.food_they_like = ["ice cream", "chocolate"]
        self.food_they_hate = ["chouchou", "calbasse"]

    def taste(self, food_name):
        if food_name in self.food_they_like:
            print(f"{self.name} eats the {food_name} and loves it!")
        elif food_name in self.food_they_hate:
            print(f"{self.name} eats the {food_name} and hates it!")
        else:
            print(f"{self.name} eats the {food_name}!")


p1 = Person("Laurent")
p1.taste("ice cream")
p1.taste("calbasse")
p1.taste("banana")