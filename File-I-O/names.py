name = input("What's your name? ")

# open: open a file. Able to read information from it or write infotmation to it

# The file where the names will be stored
# Open the file to write to this file. If the file doen't even exist, it's creates the file
# "w": recreate the file everytime you open the file in this mode
# "a": append to the bottom
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
