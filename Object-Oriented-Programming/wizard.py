# Parent class
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

# inheritance allows us to define a class that inherits all the methods and
# properties from another class
# Child class
class Student(Wizard):
    def __init__(self, name, house):
        # used to give access to methods and properties of a parent or sibling 
        # class
        super().__init__(name)
        self.house = house

# Child class
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...