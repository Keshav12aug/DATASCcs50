# fibonacci 
# 0 1 1 2 3 5 8 13
'''
def fib(n):
    #base case of recursion
    if (n==0 or n==1):
        return n 
    
    return fib(n-2) + fib(n-1)

print(fib(6))
'''

def fictorial(n):
    if (n==0 or n==1):
        return n

    return n * fictorial(n-1)

print(fictorial(5))