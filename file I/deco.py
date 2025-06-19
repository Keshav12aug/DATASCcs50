'''def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range (n):
                func(a)
        return wrapper
    return decorator
    
    
@repeat(5)
def greet(name):
    print(f"hello {name}")

greet("keshav")
'''


def decorator(func):
    def wrapper():
        print("I am about to print hello")
        func()
        print("I have executed this fuction....")
    return wrapper()


@decorator
def say_hello():
    print("Hello bro!")



class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

p = Person("Alice")

print(p.get_name())
p.set_name("BOB")
print(p.get_name())



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    

e = Employee("Jack Doe", 345000)
#print(e.first_name())
#e.set_first_name("John")
#print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)


#e.projects = 6
#print(e.projects)
