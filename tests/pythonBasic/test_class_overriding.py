class Person:

    def __init__(self,first,last,age):
        self.firstname =first
        self.lastname = last
        self.age =age

    def __str__(self):
        return self.firstname + " "+ self.lastname + " "+ str(self.age)

class Employee(Person):

    def __init__(self,first,last,age, staffnum):
        super().__init__(self,first,last,age)
        self.staffnumber = staffnum

    def __str__(self):
        return super.__str__()+ " "+ self.staffnumber


def test_class_inheritance():
    x = Person("Nannan", "Duan",23)
    y = Employee("Homer", "Simon", 23,"1008")

    assert x.Name()== "Nannan Duan"
    assert y.GetEmployee()=="Homer Simon 23 1008"
