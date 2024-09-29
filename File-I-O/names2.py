names = []

with open("names.txt", "r") as file:
    # readlines(): read all the lines from the file and return them to us as a list
    # lines = file.readlines()
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
