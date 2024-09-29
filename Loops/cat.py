# i = 3
# while i != 0:
#     print("meow")
#     i -= 1

# Allows you to iterate over a list of items
# for i in [0, 1, 2]:
#     print("meow")

# for i in range(3):
#     print("meow")

# When you don't care about the variable name
# for _ in range(3):
#     print("meow")

# Yes, you can print whatever you want multiplied by the number of times that you want
# print("meow\n" * 3)

# When you want to get user input that matches certain expectation you have
# Warning: induce an infinite loop
# while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             break

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()