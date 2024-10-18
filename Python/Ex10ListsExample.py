from itertools import count

fruits=["Apple","Mango","Orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
#
# for fruit in fruits:
#     print(fruit)
#
print(f"The no of fruits in our basket is {len(fruits)}")
print("pineapple" in fruits)
# print(dir(fruits))
#     help(fruits)
fruits.append("pineapple")
print("pineapple" in fruits)
fruits.insert(0,"Guava")
fruits.insert(3, "kiwi Fruits")
### try to remove an item from the fruits
fruits.remove("pineapple")
fruits.sort() #short the element temorarily alphabetacillay
print(fruits)
print(fruits[-2])
print(fruits[2:5])
print(fruits[:3])
print(fruits[2:])

######Modify the cntents of the list###########

fruits[1:3]=["watermelon","Dragon Fruit","pomegranate"]# Modifies the element at
# index 1 and 2
print(fruits)
# if u insert more items han U intend to replace ,the new items will be inserted
# from the location where U have specified