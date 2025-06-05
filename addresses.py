book = {}

book["tom"] = {
    'name' : 'tom', 
    'address': '1 blue street , NY', 
    'phone' : 89474737
}

book["joe"] = {
    'name' : 'Joe', 
    'address': '1 red street , NY', 
    'phone' : 24435356666
}

import json
s = json.dumps(book)

print(s)

print(book["tom"] ['phone'])

for person in book:
    print(book[person])