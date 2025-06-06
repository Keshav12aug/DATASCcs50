def sum(a,b):
    print("I am suming the two nos")
    c = a + b
    global z #please modify the value of global z 
    z = 0 #then this will refer to the global z not the local variable
    return c

z = 3

print(sum(3,20))
print(z)
