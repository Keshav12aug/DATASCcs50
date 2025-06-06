class Employee:
    company = "Asus" #the class attribute will be printed if the instance atrribute is not present

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is : {self.name}. Salary is : {self.salary}. The Bond is : {self.bond} years.")
    
        
    
e1 = Employee(34000, "John Doe", 4, "Tesla")
print(e1.get_salary())
e1.get_info()
print(e1.company)# will print instance attribute when present inside the fxn