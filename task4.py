aset = {2, 5, 6, 9, 1, 3}
print(aset)
#add 7

aset.add(7)
print(aset)

#remove 1

aset.discard(1)
print(aset)


bset = {0, 1, 3, 5, 8, 9}
print(bset)

print(aset.union(bset))
print(aset.difference(bset))
print(bset.difference(aset))
print(aset.intersection(bset))
print(aset.issubset(bset))


if 3 in aset:
    print("3 is in the aset.")
elif 3 in bset:
    print("3 is in the bset.")
else:
    print("3 is not in the aset or bset.")

