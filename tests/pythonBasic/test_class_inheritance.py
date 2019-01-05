class Person:

    def __init__(self,first,last):
        self.firstname =first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self,first,last, staffnum):
        Person.__init__(self,first,last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name()+ " " + self.staffnumber

class Student(Person):

    def __init__(self,first,last, Stunum):
        super().__init__(self,first,last)
        self.studentNum = Stunum

    def GetStudent(self):
        return self.Name()+ " " + self.studentNum

def test_class_inheritance():
    x = Person("Nannan", "Duan")
    y = Employee("Homer", "Simon", "1008")
    z = Student("Harry" , "Porter", "01")
    assert x.Name()== "Nannan Duan"
    assert y.GetEmployee()=="Homer Simon 1008"
    assert z.GetStudent() == "Harry Portter 01"