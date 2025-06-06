#Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc.

#Object: Specific instance created from template (class), Eg from which contains the data for John Doe

class Employee:
    company = "HP"

    def get_salary(self):
        return 34000
    
e1 = Employee() #objact of class Employee is created here 
print(e1.get_salary()) #Employee e's get salary method is called
print(e1.company)

e2 = Employee()
print(e2.get_salary())
print(e2.company)
