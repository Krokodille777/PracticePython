ginnysDict = {
    "fname": "Ginny",
    "lname": "Gray",
    "title": "The Marionette",
    "age": 13,
    "father": "Foster Gray (The Puppeteer)",
    "mother": "Eleonora Gray (The Witch)",
    "lives in":"The House of Grays",
    "abilities": ["Healing", "Flying", "Baking", "Dancing", "Fight"],
    "second_mother": "Lyra",
    "hates": ["The Order", "Meanies", "spicy_food", "boredom"]
}

print(ginnysDict)

#1 Add Item 

new_item = {"best_friends": ["Toto", "Veronika"]}

ginnysDict.update(new_item)


#2 Nested Dictionary

lovesDict = {
    1: "Toto",
    2: "Adventure",
    3: "Her family",
    4: "Knight Novels",
    5: "Vikings"
}

ginnysDict["loves"] = lovesDict
print(lovesDict[3])

#3 Remove Item

del ginnysDict["hates"]
print(ginnysDict)

#4 and 5 keys() and values()

for x in ginnysDict.keys():
    print(x)

for y in ginnysDict.values():
    print(y)

#6 and 7 items() and update()
for x, y in ginnysDict.items():
    print(x, y)
new_item2 = {"favorite_phrase": "You're all Big Meanies!"}
ginnysDict.update(new_item2)

print(ginnysDict)