#write a file called JohnDoe.txt
#it should contain the data related to jonh doe


f = open("JohnDoe.txt", "w")

string = " John is a nice guy, he is workaholic, he works on python.\nHe creates a new file.\nHe is a genius. "

f.write(string)

f.close()

