class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def __str__(self):
        return f"{self.id_number} {self.name}"


class Queue:
    def __init__(self):

        self.humans = []

    def add_person(self, person):
        if person.age >= 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        return self.humans.index(person)

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if not self.humans:
            return None

        return self.humans[0]

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if human.blood_type == blood_type:
                return self.humans.remove(human)

    def sort_by_age(self):
        return self.humans.sort(key=lambda human: human.age)

    def print_list(self):
        for human in self.humans:
            print(human)


Laurent = Human("123", "Laurent", 34, False, "A")
Josiane = Human("234", "Josiane", 70, False, "B")
Manu = Human("456", "Manu", 80, False, "0")
Elodie = Human("789", "Elodie", 60, True, "AB")

queue = Queue()
queue.add_person(Laurent)
queue.add_person(Josiane)
queue.add_person(Elodie)
queue.add_person(Manu)

print(queue.find_in_queue(Laurent))
print(queue.find_in_queue(Josiane))
print(queue.find_in_queue(Manu))
print(queue.find_in_queue(Elodie))

queue.swap(Laurent, Manu)
print(queue.find_in_queue(Laurent))
print(queue.find_in_queue(Josiane))
print(queue.find_in_queue(Manu))
print(queue.find_in_queue(Elodie))

print(queue.get_next())
queue.print_list()
queue.sort_by_age()
queue.print_list()

print(queue.get_next_blood_type("B"))
queue.print_list()


