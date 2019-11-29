#  !/usr/bin/python

# In this program we are going to display the name, age and height of a person
# Concepts discussed related to the program are given in the comments


print("*** Demo : Python does not need data type declaration ***")

age = 20
height = 6.15
name= "Munna Bhai"

#print() is used in python 3 onwards
print("Age is ",age)
print("Height is ",height)
print("Name is ",name)

# To run below line use python2 print age at command prompt 
# print age

print("*** Demo: Multiple Assignment in one line is possible in python. The data given can be of different data types")

age, height, name = 51,5.91,"Mogambo"

print("Name is ",name)
print("Age is ",age)
print("Height is ",height)

print("*** Demo Polymorphic Variable: Variables are not bound to a data type once assigned")

age = 51.0

print("Age is ",age)
print("Name is ",name)
print("Height is ",height)
