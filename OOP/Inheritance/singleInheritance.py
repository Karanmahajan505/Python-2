
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getinfo(self):
        return f"Name : {self.name} Age : {self.age} Salary : {self.salary}"

class Manager(Employee):
    def __init__(self,name, age, salary,department):
        super().__init__(name,age , salary)
        self.department = department

    def getinfo(self):
        return f"{super().getinfo()} Department : {self.department}"   
    
new_Manager = Manager("Atharv",20,100000,"IT")
print(new_Manager.getinfo())