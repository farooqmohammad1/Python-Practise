# # a="hello world"
# # print(a[0])
# # print(a[1])

# a='''Hello Everyone
# welcome back to my
# python tutorial'''
# print(a[1])
# print(a[10])

# looping in strings

# for a in "bababa":
#     print(a)

# a="Hello World"
# print(len(a))

# fruit="Mango"
# len=len(fruit)
# print("Mango is a",len,"letter Word")
# name="Hello Everyone"
# print(name[0:7])

# The upper() method returns the string in upper case:
# name="farooq"
# print(name.upper())
# name1="FAROOQ"
# print(name1.lower())

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.


# The strip() method removes any whitespace from the beginning or the end:

# text=" My Name is "
# print(text.strip())

# The replace() method replaces a string with another string:
# name="Hello World Hello"
# print(name.replace("H","L"))

# The split() method splits the string into substrings if it finds instances of the separator:

# a = "Hello, World!"
# print(a.split("l")) #  ['He', '', 'o, Wor', 'd!']
# print(a.split("!"))  :::=> ['Hello, World', '']
# print(a.split(","))  ['Hello', ' World!']

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} ar

# name="Hi {}"
# n="farooq"
# print(name.format(n)); Hi farooq

# age = 36
# txt = "My name is John, and I am  {} years old"
# print(txt.format(age))  ::My name is John, and I am  36 years old

# name=input("Enter your Name")
# group=input("Enter your Group")
# final="Your Name is  {} and Your Group is {} "
# print(final.format(group,group)) Your Name is  b and Your Group is b
# print(final.format(name,group))  Your Name is   g and Your Group is b 

# quantity = 3
# itemNo = 567
# price = 49.95
# myOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myOrder.format(quantity, itemNo, price)) I want to pay 49.95 dollars for 3 pieces of item 567.

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# count method
# The count() method returns the number of times a specified value appears in the string.

# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple",1,19)
# x=txt.count("fruit")
# x=txt.find("fruit") 	Searches the string for a specified value and returns the position of where it was found

x = "Hello"
y = 15

print(bool(x))
print(bool(y))





  