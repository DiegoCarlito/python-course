students = ["Hermione", "Harry", "Ron"]

# Dictionary Comprehensions
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

# Enumerate
for i, student in enumerate(students):
    print(i + 1, student)