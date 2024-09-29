def main():
    yell("This", "is", "CS50")

"""
The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter.

map(function, iterables)

function: Required. The function to execute for each item
iterable: Required. A sequence, collection or an iterator object. You can send
as many iterables as you like, just make sure the function has one parameter for
each iterable.
"""

def yell(*words):
    uppercased = map(str.upper, words)
    # List Comprehensions
    # uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()