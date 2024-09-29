"""
Regex: use patterns to match on some kind of data, often user input

. -> any character except a newline
* -> 0 or more repetitions
+ -> 1 or more repetitions
? -> 0 or 1 repetitions
{m} -> m repetitions
{m,n} -> m-n repetitions

^ -> matches the start of the string
$ -> matches the end of the string or just before the newline at the end of the
string

[] -> set of characters
[^] -> complementing the set

\d -> decimal digit
\D -> not a decimal digit
\s -> whitespace characters
\S -> not a whitespace character
\w -> word character ... as well as numbers and the underscors
\W not a word character

A|B -> either A or B
(...) -> a group
(?:...) non-capturing version
"""
import re

email = input("What's your name? ").strip()

# re.search(pattern, string, flags=0)
# r means raw string
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:    
    print("Invalid")