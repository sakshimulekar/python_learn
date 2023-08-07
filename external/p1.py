#store variables in python

#four diff data type: number, string, float, boolean

name = "aman"
age = 22
is_adult = False

#print(name,age,is_adult)

#name = input("enter your name: ")
#print("Hello "+name)

#if there is number it will store in string formate. to avaoid that concatination, put 'int' keyword at begins, it will convert into number form.

# first = input("enter first number: ")
# second = input("enter second number: ")
# sum = int(first) + int(second)
# print(sum)

#-------------------------------------------------------#
#string
# there are some inbuild method which helps to do specific operation on string. i.e. upper(),lower(),find(),replace()

# upper(): it will form new string, instead of modifying the original string
# name = "Tony Stark"
# print(name.upper())

#lower():same as above, create new string.
# name = "John Shein"
# print(name.lower())
# print(name)

#find:search the substring. return us the index of substring. if substring is not availabe then it will return '-1'
name = "tony Stark"
print(name.find('t'))

# replace : it replace the substring
name = "Tony Stark"
print(name.replace("Stark","Ironman"))      #Tony Ironman
print(name.replace("T","M"))    #Mony Stark
print(name)   #Tony Stark

# 'in': it will check for the substring, if its available then it return boolean value.
print("S" in name)      #True
print("stark" in name)      #False

# operators: +, - , * , / , // , % , **
# += , -= , *= 
# operator precedence
# '//' it will return integer value only. i.e. 6.9 //6
# comparision operatore: > , < , >= ,<= , == , != 
# Logical operatore : or, and,not




