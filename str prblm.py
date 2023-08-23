# name=input("Enter Your name")
# print("Hi",name)

# 2.
letter='''Hi <NAME>
you are selected
Date:<DATE>
'''
name=input("Enter your Name")
date=input("Enter date")
letter=letter.replace("<NAME>",name)
letter=letter.replace("<DATE>",date)
print(letter)
