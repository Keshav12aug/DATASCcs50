import requests

r = requests.get('https://api.github.com/users/keshav12aug')

with open("Keshav12aug.txt", "w") as f:
    f.write(r.text)