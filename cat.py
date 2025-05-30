'''
i = 0
while i < 3:
    print("Meow")
    i +=1
    '''

'''for i in range (3):
    print("meow")
'''
# in case we don't wanna use loops

# print("meow\n" * 3, end = "")

'''
while True:
    n = int(input("What's n? "))
    if n > 0:
     break

for i in range (n):
    print("Meow")
'''

def main():
    meow(3)

def meow(n):

    for i in range(n):
        print("meow")

main()




