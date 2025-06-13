'''with open ("demo.txt", "a") as f:
    f.write("I am learning file I/O\n")'''

#writing and replacing a file
'''
with open ("q1.txt", "r") as f:
    #f.write("Hi everyone\nwe are learning File I/O\nusing python.\nI like programing in python.")
    data = f.read()

new_data = data.replace("python", "Java")
print(new_data)
with open("q1.txt", "w") as f:
    f.write(new_data)
'''
#finding a letter/word
def check_for_word():
    word = "learning"
    with open("q1.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_for_word()
