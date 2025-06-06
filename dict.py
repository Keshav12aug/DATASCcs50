d = {"Tom" : 7345453554,
     "Harry" : 648363489, 
     "brad" : 734353566
     }

d["sam"] = 8348397375

print(d)

del d["sam"]

print(d)

for k, v in d.items():
    print("key : ", k, " value : ", v)

print("Tom" in d)


#tuple
'''
point = (5,9)
point[0]
point[1]
'''