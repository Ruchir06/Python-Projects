# name = input("Enter your name: ")
# print(name)
# result = name.rfind("r")
# print(len(name))
# print(result)

# name = name.capitalize()
# print(name)

# name = name.upper()
# print(name)
# name = name.isdigit()
# print(name)

# name = name.lower()
# print(name)

# name = name.isalpha()
# print(name)


# phone = (input("Enter a phone number: "))
# result = phone.count("9")
# print(result)


username = input("Enter your username: ")

if len(username) > 12 or username.count(" ") > 0 or username.isalpha(): 
    print("The username is invalid")
else: 
    print(f"You username is {username}")
