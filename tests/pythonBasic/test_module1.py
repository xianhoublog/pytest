import moduletest

def test_module():

    assert str(moduletest.ageofqueen) == "78"
    assert moduletest.printhello() == "hello"
    cfcpiano = moduletest.Piano()
    cfcpiano.printdetails()

