name = input("What's your name ? ")

if name == "Harry".lower() or name == "Ron".lower() or name == "Hermoine".lower():
    print("Gryffindor")


elif name == "Draco".lower:
    print("Slytherin")

else:
    print("Who?")


'''
name = input("What's your name ? ")

match name:
    case "Harry" | "Hermoine" | "Ron" :
        print("Griffindor)
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

'''