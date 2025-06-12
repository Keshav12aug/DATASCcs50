def decorator(func):
    def wrapper():
        print("I am about to print hello.....")
        func()
        print("I have executed this fuction....")
    return wrapper



def say_hello():
    print("Hello!")

say_hello()
decorator(say_hello)