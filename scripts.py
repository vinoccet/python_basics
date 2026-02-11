# classes and objects
# its a template that defines properties and behaviour
# properties -> member variable
# behaviour -> methods

# public, protected and private

class Fruits:
    def __init__(self,color,type,vitamins):
        self.color=color
        self.type=type
        self.vitamins=vitamins

apple=Fruits("red","watery","B12")
apple.color="green"
print(apple.color)

class Employee:
    def __init__(self,name,age,department,designation):
        self.name=name
        self.age=age
        self.department=department
        self.designation=designation

    def getSalary(self,salary):
        print("salary")

    def getDepartment(self):
        print(f"department is {self.department}")    

    def getDesignation(self):
        print("designation  is {self.designation}")    

emp1=Employee("emp1",38,"cse","M")
emp2=Employee("emp2",39,"HR","SM")
emp3=Employee("emp3",20,"Operational","PA")
emp1.getDepartment()
emp2.getDepartment()
emp3.getDepartment()