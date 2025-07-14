# returns the lenght of the string chaacters including the space len()
name = "khaled sabry"
print(len(name))
# returns the index of the first occurance of the letter in the string .find()
print(name.find("k"))
# returns the last occurance of the letter inside a string .rfind()
print(name.rfind("a"))
# captalize the first letter of a string .captalize()
print(name.capitalize())
# change the whole string to upper case .upper()
print(name.upper())
# change the whole string into lower case .lower()
print(name.lower())
# check if the whole string contains digit isdigit()
print(name.isdigit())
# check if the whole number is alpha will return false if contains space .isalpha()
print(name.isalpha())
# count number of occurance of certain letter inside a string .count()
print(name.count("a"))
# replaces a certain char in string with a given replacment .replace
name.replace("a", "-")

# ex check if username is more than 12 chars , must not contain spaces . must not contains digits

username = input("enter your username: ")

if not username.isalpha or len(username) > 12:
    print("invalid username !!")
else:
    print("good one ✌️")
# indexing strings , act as an array [start:end:step] negative indexing will get from the last order
print(name[0:4:2])
# you can use -ve indexing in step to reverse a string
print(name[::-1])
