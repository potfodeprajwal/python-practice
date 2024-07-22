# write a Python program to display user entered name followed by good afternoon using input()
a = input("enter your name :")
print(f"Good Afternoon, {a}")


# write a program to fill in later template given below with the name and date
# '''Dear <|name|>
#  You are slected !
# <|date|>'''

name = input("Enter your name :")
date = input("Enter date :")
print(f"Dear {name}\nYou are slected !\n{date}")

letter = '''Dear <|name|>
You are slected !
<|date|>'''
print(letter.replace("<|name|>","Prajwal").replace("<|date|>","23 July"))


# write a program to detect double space in a string
detect = "prajwal is good boy"
print(detect.find("  "))  #if it returns -1 means there is no double space

tu = "prajwal is    good   boy"
print(tu.find("  ")) 


