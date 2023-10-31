class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

obj=Manager("John",1000,"Mechanical")
obj.display()
        
