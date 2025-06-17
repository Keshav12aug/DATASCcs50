#decorator is a function that takes a function, it creates a new function inside its body(wrapper). Then it returns that new function

def decorator(func):
    def wrapper():
        print("I am about to print hello.....")
        func()
        print("I have executed this fuction....")
    return wrapper


@decorator
def say_hello():
    print("Hello!")

say_hello()


'''f = decorator(say_hello)
f()'''