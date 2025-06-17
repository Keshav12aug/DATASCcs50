class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    #static method 
    @staticmethod
    def sum(a, b): #when I don't wanna add self to a fxn
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 3455)
#print(Employee.company)
# #print(Employee.name) this will throw an error 

e1.print_info()
e2.print_info()

print(e2.sum(5,28))

e1.print_company()

e1.change_company("Acer")
e1.print_company()
print(Employee.company)