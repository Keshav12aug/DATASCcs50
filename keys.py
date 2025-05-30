key_location = "Chair"
locations = ["Garage", "Living room", "Dinning Table", "Chair", "Closet", "Bedroom"]

for i in locations:
    if i == key_location:
        print("Key is found in", i)
        break
    else:
        print("Key is not found in ", i )

