class Animal:
    location = "Austrilia"
    
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal is Speaking now.....")

class dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

#a = Animal("Dog")
#a.speak()
d = dog("Bruno")
d.speak()
print(d.location)


