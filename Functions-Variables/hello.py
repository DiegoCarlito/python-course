# Python has dynamic type
# Python is an interpreted language
# You don't necessary have to write pyhton in a file (Interactive mode)
# To access interactive mode, run "python" or "python3" in terminal

# Scope: your variable only exists in the context you defined

def main():
    hello()

    # Ask user for their name
    name = input("What's your name? ")

    hello(name)

# Let's create a function that says hello
# In this case we define a parameter for the function
# You can define a default value in case the programmer doesn't call
# hello() with a argument
def hello(name="world"):
    print(f"Hello, {name}!")

main()

"""
multiline comment in
python
"""

# + concatenation
# , separate arguments

# Say hello to user
# print("hello, " + name)
# print("hello,", name)

# You can chain the methods
# Is this a good practice?
# Answer: code needs to be easy to read and understand

# Remove whitespace from string and Capitalize user's name
# name = name.strip().title()

# Split user's name into first name and last name
# split return a sequence of values
# first, last = name.split(" ")

# Capitalize user's name
# name = name.capitalize()
# name = name.title()

# Format string
# print(f"hello, {first} {last}")
