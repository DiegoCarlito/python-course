# arithmetic operators: + - * / % **
# data types: string, int, float

# How to round float numbers?
# round(number) - nearest possible integer
# round(number[, ndigits]) - specify the number of digits that you want

"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(round(x + y))
print(z)
"""

# We can specify how many digits we want in the number using format string
# print(f"{z:.2f}")

# return: returns a value

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)

main()