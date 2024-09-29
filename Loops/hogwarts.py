# List: set of multiple values
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Let's iterate over students
# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# Dictionary: data structure that allows you to associate one value with another
# Let's associate a student with a house
# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin",
# }

# Dictionaries allow you to use words as your indexes
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

# Let's do a list of dictionaries
# None: represents the absence of a value
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")