import re

name = input("Wha's your name? ").strip()

# walrus operator: allows you to assign a value and ask a boolean question
#   - Assignment expression operator
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")