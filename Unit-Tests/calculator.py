# A Really good practice to break your ideas up into smaller bite-sized that themselves are 
# testable.
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
