# x = int(input("Enter a number : "))

# if x % 2 == 0:
    # print("The number is Even")


# else:
    # print("The number is odd")

'''by using def fxn'''

def main():
    x = int(input("Enter a number : "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return  (n % 2 == 0)

    
main()