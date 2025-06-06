indian = ["samosa", "jalebi", "dal", "naan", "paneer"]
chinese = ["noodles", "manchurian", "fried rice", "chilly paneer"]
italian = ["pizza", "pasta", "burchetta", "lasagne"]

dish = input("Enter the name of a Dish : ")

if dish in indian:
    print("The Dish you have entered is indian")
elif dish in chinese:
    print("The Dish you have entered is chinese")
elif dish in italian:
    print("The Dish you have entered is italian")
else:
    print("undetectable")
    