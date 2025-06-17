def sum(*args):
    #args will be a tuple of all the value passed to sum
    print(args)
    total = 0 
    for item in args:
        total += item
    return total


print(sum(342, 2, 7, 9)) 


