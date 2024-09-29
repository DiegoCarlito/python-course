def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

"""
The yield keyword is used to return a list of values from a function.

Unlike the return keyword which stops further execution of the function,
the yield keyword continues to the end of the function.

This allows its code to produce a series of values over time, rather than
computing them at once and sending them back like a list.
"""

def sheep(n):
    for i in range(n):
        yield "🐑" * i
    # flock = []
    # for i in range(n):
    #     flock.append("🐑" * i)
    # return flock

if __name__ == "__main__":
    main()