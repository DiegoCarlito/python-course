students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

# The set() function creates a set object
houses = set()
for student in students:
    # This has no effect if the element is already present
    houses.add(student["house"])

for house in sorted(houses):
    print(house)