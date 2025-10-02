class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("department=",self.department)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name)
        print("age=",self.age)
        super().__init__("Engineer","IT","75000")

e1=Employee("accountant","finance","60000")
e1.showDetails()
e2=Engineer("elon musk",40)
e2.showDetails()