""" 
Procedural Programming: a programming paradigm built arround the idea that
programs are sequences of instructions to be executed.

Example:
name = input("Name: ")
house = input("House: ")
print(f"{name} form {house}")

Object-Oriented Programming (OOP): is a computer programming model that organizes
software design around data, or objects, rather than functions and logic. An object
can be defined as a data field that has unique attributes and behavior.

Classes: a class is a blueprint for creating objects(a particular data structure),
providing initial values for state (member variables or attributes), and
implementations of behavior(member functions or methods).

The user-defined objects are created using the `class` keyword. The class is a
blueprint that defines a nature of a future object.

An instance is a specific object created from a particular class.

Classes are used to create and manage new objects and support inheritance.
"""

# Dunder methods: Double Under(Underscores)
# - They are defined by built-in classes in Python and commonly used for operator
# overloading


class Student:
    # The __init__ method for initialization is invoked without any call, when 
    # an instance of a class is created, like constructors in certain other 
    # programming languages.
    # The `self` variable represents the instance of the object itself
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # returns a human-readable, or informal, string representation of an object
    def __str__(self):
        return f"{self.name} form {self.house}"
    
    # Getter = function in some class that gets some attributes
    # In python, properties are a type of attribute that allow for controlled
    # access to an object's internal data
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    # Setter = function in some class that sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()