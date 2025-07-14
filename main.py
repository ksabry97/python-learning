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

# logical operators or , and , not , !=

# weight converter
weight = float(input("enter your weight: "))
unit = input("enter the unit wehter kg or lbs (k / l): ")

if unit != "k" and unit != "l":
    print("this is not a valid unit")
elif unit == "k":
    weight *= 2.205
    unit = "lbs"
    print(f"your weight is {weight} {unit}")
else:
    weight /= 2.205
    unit = "kgs"
    print(f"your weight is{weight} {unit}")
# condtional expression to print if else in one statment
# x if condition else y
num = 5
new_value = "even" if num % 2 == 0 else "odd"
print(new_value)
