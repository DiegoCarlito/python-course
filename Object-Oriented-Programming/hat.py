import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # classmethod must have a reference to a class object as the first
    # parameter
    # it doesn't require creation of a class instance, much like static method
    # cls = class
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")   