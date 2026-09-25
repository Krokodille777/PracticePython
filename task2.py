atuple = (2, 3, 5, 8, 13, 21, 34, 55, 89)
print(atuple)

#1. if A in B

if 21 in atuple:
    print("21 is in the tuple.")

if 5 in atuple:
    print("5 is in the tuple.")
if 64 in atuple:
    print("64 is in the tuple.")
else:
    print("64 is not in the tuple.")

#2 Slicing

print (atuple[2:5])

#min and max and add it

print (min(atuple))
print (max(atuple))

print (min(atuple) + max(atuple))

#From tuple to list and vice versa

btuple= list(atuple)
btuple[4] = 15
atuple = tuple(btuple)
print(atuple)

#unpacking
ctuple = ("lemon", "grapes", "strawberry", "cherry", "raspberry")

(yellow, purple, *red) = ctuple
print(yellow)
print(purple)
print(red)



for i in range(len(atuple)):
    print(atuple[i])




