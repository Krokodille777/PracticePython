characters = ['Ginny', "The Puppeteer", "Lyra", "Mara", "Veronika","Balthazar", "Toto" , "Elder Thorne"]
print(characters)
#1
if "The Puppeteer" in characters:
    print("The Puppeteer is in the list.")

if "Toto" in characters:
    print("Toto is in the list.")

if "Ragnar" in characters:
    print("Ragnar is in the list.")
else:
    print("Ragnar is not in the list.")


#2

selected_characters = characters[3: 6]
print(selected_characters)

#3 Add Gregor

if "Gregor" not in characters:
    characters.append("Gregor")
    print (characters)

#Add Eleonora

if "Eleonora" not in characters:
    characters.append("Eleonora")
    print (characters)

#4 Remove Balthazar

if "Balthazar" in characters:
    characters.pop(characters.index("Balthazar"))
    print(characters)

#5 Create a nest list and print one of it's elements

more_characters= [characters, ["King Edward", "Princess Camille", "Lorenzo", "Rotter'Art", "Lord Arin", "Sabba'Art"]]

print(more_characters[1][3])

#6 Print every element from more_characters, using for and len

for creature in range(len(characters)):
    print(characters[creature])

#7 Sort more_characters in alphabetic order and print it


for creature in range(len(characters)):
    characters.sort()


print(characters)

#8 Use count() method

print(characters.count("Lyra"))

#9 Use index() method

print(characters.index("Toto"))

