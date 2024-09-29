# try:
#   (try something)
# except (what error do you want to catch):
#   (if something goes wrong, do something else)

# It's good pratice to define the type of error you want to capture
# pass: ignore

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

main()