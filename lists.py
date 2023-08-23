# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.[]

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()

# Set is a collection which is unordered, unchangeable*, and unIndexed. No duplicate members.{}

# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.




# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:


# list1=[1,2,3,4,5,6,7,8,9]
# print(list1)

# list2=["abc","bca","cab"]
# print(list2)

# list2[0]="jk"
# print(list2)

# list3=[True,False,True]
# print(list3)
# print(type(list3))

# list4=["ab",1,2,True,"far",False]
# print(type(list4))
# print(list4)

# Since lists are indexed, lists can have items with the same value:
# thisList = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thisList)
# print(len(thisList))

# It is also possible to use the list() constructor when creating a new list.

# Example
# Using the list() constructor to make a List:

# thisList = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisList)
# print(type(thisList))

# thisList=list(("apple",1,2,False,"banana"))
# print(thisList)
# print(type(thisList))

# list Slicing
# list1=[1,2,3,4,5,6,7,89]
# print(list1[:-1])

# 
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-1:-4])

thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#   print("no Yaar apple anahi hai")

# changing list items
# thislist[1]="cheese"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]  ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)  ['apple', 'blackcurrant', 'watermelon', 'cherry']

# insert Method
# num=[1,2,3,6,7,8,9,]
# num.insert(4,5)  [1, 2, 3, 6, 5, 7, 8, 9]
# num.append(45)  [1, 2, 3, 6, '5', 7, 8, 9, 45]
# num.append(5678)  [1, 2, 3, 6, '5', 7, 8, 9, 45, 5678] 
# print(num)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)  ['apple', 'orange', 'banana', 'cherry']
# thislist.insert(0,"sad")
# print(thislist)  ['sad', 'apple', 'orange', 'banana', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)  The elements will be added to the end of the list.
# print(thislist)  ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
# tropical.extend(thislist)
# print(tropical)  ['mango', 'pineapple', 'papaya', 'apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)