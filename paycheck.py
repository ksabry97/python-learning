item = input("what item do you wanna buy ?:")
price = float(input("what is the price per item ?:"))
quantity = int(input("how many do you want ?:"))
total = price * quantity
print(f"total is:{total}")
paid = float(input("your check:"))
if paid < total:
    print("this not enough")
    float(input("your check:"))
else:
    remainder = paid - total
if remainder:
    print(f"your remainder is : {remainder}")
else:
    print("thank you..!!")

# problem will be solved when we know how to write a function 😂
