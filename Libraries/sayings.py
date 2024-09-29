def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# __name__: is a special variable managed by Python and 
# it will automatically set its value to “__main__” if 
# the script is being run directly and to the name of the 
# module, that is, its filename, if it is just being automatically 
# executed as part of an import statement.
if __name__ == "__main__":
    main()