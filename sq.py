#print square of no's in range 1 to 11 except even numbers 

for  i in range (1,11):
    if i % 2 == 0:
        continue
    else:
        print(i * i)
