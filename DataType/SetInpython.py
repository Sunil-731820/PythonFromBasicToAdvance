set1 = set()
print("the empty set is ")
print(set1)
set11 = set("GeeksforGeeks")
print("the new set is ")
print(set11)

#creating the set of the list of the objects using set()

set21 = set(["Geeks","For","Geeks"])
print("the set of the given list of the obejcts is ")
print(set21)

#adding the element to the set

set221 = set()
print("the empty set is ")
print(set221)
set221.add(31)
print("the new set is ")
print(set221)
print("after adding new element to the set is ")
set221.add("sunil")
print("the set is ")
print(set221)
print("adding the multiple element to the set is ")
set221.add((6,7))
print("the new set is ")
print(set221)
print("adding the list of the objects is ")
set221.update(["suman","Arti"])
print("the new set is ")
print(set221)

set33 = set(["Geeks","for","Geeks"])
print("the set is ")
print(set33)
for i in set33:
    print(i ,end=" ")
print()
print("Geeks" in set33)

