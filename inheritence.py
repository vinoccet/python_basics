# is-a relationship - inheritance
# polymorphishm - compile time and runtime polymorphism
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getSalary(self,salary=100):
        print(f"salary is {salary}")

    def getLeaveDetails(self):
        print("Total cl in year is 12")    


class ITEmployee(Employee):
    def __init__(self,name,age,skill):
        super().__init__(name,age)
        self.skill=skill

    def getLeaveDetails(self):
        print("Total cl in year is 10 days")    

emp1=ITEmployee("emp1",38,"python")
print(emp1.age)
print(emp1.skill)

emp1.getSalary()
emp1.getSalary(1000)

len("vinoth")
len([1,2,4])
len((1,4,7,8))