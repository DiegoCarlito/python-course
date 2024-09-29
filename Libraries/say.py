# pip install cowsay
import cowsay
import sys
from sayings import hello, goodbye

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    hello(sys.argv[1])
    goodbye(sys.argv[1])

# APIs: Application Programming Interface
# - refer to python files and functions
# - refer to third-party service

# requests: very popular package that allows you to make web requests
# - pip install requests