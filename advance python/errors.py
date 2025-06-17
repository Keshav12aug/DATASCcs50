while True: #going in the infinite loop where the program keeps on running
    try:
        a = int(input("Enter the number 1 : "))
        b = int(input("Enter the number 2 : "))
        print(f"The sum is {a + b}")

    except: 
        print("Some error occured")