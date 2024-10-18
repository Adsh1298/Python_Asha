#sets:unordered and immutable collections but can hold only unique values in it .
#it can allow to add and remove the items from it
#sets are created using{}braces.

names={"phani","Vinod","Banu","Ramnath","JoyDip"}
print(names)
print(names)
print(names)
print(names)
#print the values in unordered manner
for name in names:
   print(name)#print(names[1])
names.add("Murali")
print(names)

# Adding bulk records:
trainers={ "Krishna","Nathan","Somnath"}#Adding another set into the current set
names.update(trainers)
print(names)
 #Removing items from the set:
 #remove and discard function: remove throws an error if an item is not found to
# remove from set,but discard shall not throw any exception
names.remove("Krishna")
print(names)
names.discard("somnath")
print(names)
#How many ways can we remove items in collection:4ways: remove.disard,pop and clear

