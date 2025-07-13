# teplate string used to get a formatted string with a certain variable
import math
name = "Khaled Sabry"
print(f"hello {name}")
isBoolean = True
print(f"{isBoolean}")
# convert from data type to another using str() , int(), float(), bool()
if name:
    print('yes')
else:
    print('no')
# getting data from input() function is always string
extract = input("what's your name?:")
age = input("give me your age : ")
print(f"my age is {age}")
print(f"my name is {extract}")

# ex1 calculation of an area of rectangle

length = int(input("length : "))
width = int(input("width:"))
area = length * width
print(area)
