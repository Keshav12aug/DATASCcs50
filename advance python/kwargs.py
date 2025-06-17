def marks(**kwargs):
    #kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")


marks(shubham = 34, sahil = 45, aman = 76, naman = 87)