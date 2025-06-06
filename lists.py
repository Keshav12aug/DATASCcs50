items = ["Bread".lower(), "butter", "Pasta", "Fruits", "Vegetables"]
fruits = ["apple", "banana", "kiwi"]

print(items)

print(items[1:4])

items.append("Chips")

print(items)

print(len(items))

items.insert(2, "biscuits")

print(items)

fruits.append("dragon")

groceries = items + fruits

#also 
items.extend(fruits)

print(groceries)

print(len(groceries))

print("bread" in items)