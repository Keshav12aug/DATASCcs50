marks1 = int(input("Enter marks 1 : "))
marks2 = int(input("Enter marks 2 : "))
marks3 = int(input("Enter marks 3 : "))
marks4 = int(input("Enter marks 4 : "))
marks5 = int(input("Enter marks 5 : "))
marks6 = int(input("Enter marks 6 : "))

#check for the total percentage

total_percentage = (100*(marks1 + marks2 + marks3 + marks4 + marks5 + marks6))/600
print("Your total percentage is : ", total_percentage)

if(total_percentage>=33 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33 and marks5>=33 and marks6>=33):
    print("You are pass")
    
if(total_percentage<=100 and total_percentage>=90):
    grade = "O"
elif(total_percentage<90 and total_percentage>=80):
    grade = "A+" 
elif(total_percentage<80 and total_percentage>=70):
    grade = "A"
elif(total_percentage<70 and total_percentage>=60):
    grade = "B"
elif(total_percentage<60 and total_percentage>=50):
    grade = "C"
elif(total_percentage<50 and total_percentage>=40):
    grade = "E"
elif(total_percentage<33):
    grade = "F"
else:
    print("You are failed")
    
print("Your grade is : ", grade)