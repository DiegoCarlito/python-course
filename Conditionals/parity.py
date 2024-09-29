def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# The is_even() function returns a boolean value
def is_even(n):
    return n % 2 == 0

# def is_even(n):
#     return True if n % 2 == 0 else False

main()