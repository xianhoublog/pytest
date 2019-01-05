from moduletest import ageofqueen
from moduletest import printhello

def test_module():

    assert str(ageofqueen) == "78"
    assert printhello() == "hello"


