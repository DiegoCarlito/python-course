import csv
students = []

# The with statement in Python helps you with resource management. It ensures you don't 
# accidentally leabe any resources open
# Replaces a try-catch block
# It ensures closing resources right after processing them

# No csv module
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name": name, "house": house}
#         students.append(student)

with open("students.csv") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# Python allows to pass functions as arguments into other functions
# tip 1: reverse=True
# tip 2: instead of using "key=" to refer to a function name like "key=get_name", we can use a 
# lambda function, because we only use the function in this case
# lambda: a lambda function is a small anonymous function.
#   - A lambda function can take any number of arguments, but can only have one expression
#   - Syntax: lambda arguments : expression
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
