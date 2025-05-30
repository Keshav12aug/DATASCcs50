'''students = ["Harry", "Hermoine", "Ron", "Draco", "Voldermort"]

for i in range(len(students)):
    print(i +1, students[i])
'''

#dictionaries

students = {
    "Hermione" : "Gryffindor" ,
    "Harry"    :  "Gryffindor",
    "Ron"      : "Gryffindor",
    "Draco"    : "Slytherin",
}
for s in students:
    print(s, students[s], sep = ", ")

