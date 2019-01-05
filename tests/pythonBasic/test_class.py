class NannanClass:
    name = "nannan"
    def sum(self,a,b):
        return(a+b)

def test_calss():
    x=NannanClass()
    assert x.name  == "nannan"
    assert x.sum(3,4) == 7

class NannanClass2:
    name = "nannan2"
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def sum(self, a, b):
        return a+b

def test_NannanClass2():
    x = NannanClass2("john","23")
    assert x.name == "nannan"
    assert x.sum(3, 4) == 7