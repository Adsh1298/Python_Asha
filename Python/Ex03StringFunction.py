name="asha kumari"
#No of character in the string:len
print(len(name))
print(name.capitalize())
print(name.title())
print(name.upper())

#Find out if the string has a number:
print(name.isdigit())
#Finf out if the string has only aplhabets:
print(name.isalpha())
#Finf out a character in string:
print(name.find('a'))
#Find and replace
print(name.replace('a','aa'))
print(dir(name))
help(type(name))

a=123
print(id(a))
