# Make tests simple and small
# the file __init__.py tells to python to treat the folder test as a package
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Diego") == "hello, Diego"
