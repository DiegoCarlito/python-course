import sys

# command-line arguments: allows you to provid arguments when you're
# executing it at a command line

# IndexError: An IndexError is often encountered when you attempt to 
# access an index in a sequence, such as a list, tuple, or string, and 
# it is outside the valid range. 

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError: 
#     print("Too few arguments")

# Check for errors
if len(sys.argv) < 2:
    # if the user has not provided us with the data we want, simply exit the program early
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# It's a good pratice keeping all your error handling separete from the code
# that you realy care about

# Print name tags
# print("hello, my name is", sys.argv[1])

# slice of a list means to take a subset, [begin:end]
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# packages: a module essentially implemented as a folder
# - generally is a third-party library
# - where can i get all these packages? A: PyPI (pypi.org)
# - python package manager: pip