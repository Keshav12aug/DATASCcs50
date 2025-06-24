try:
    a = float(input("Enter first number: "))
    b = float(input("Enter the second number: "))

    print("What kind of operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press / for division")
    print("Press * for multiplication")

    o = input("Enter Operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "/":
            print(f"The result is: {a / b}")
        case "*":
            print(f"The result is: {a * b}")
        case _:
            print("Invalid operation")

except Exception as e:
    print("Enter a valid number for a and b.")
 