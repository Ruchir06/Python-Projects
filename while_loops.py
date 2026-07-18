# age = float(input("Enter youa age: "))

# while(age <= 0):
#     print("Invalid age")
#     age = float(input("Enter your age: "))
# print(f"You are {age} years old")


# if (name == "" ):
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")


num = int(input("Enter a number: "))
while(num > 10 and num < 0):
    print(f"{num} is not valid.")
    num = int(input("Enter a number"))

print(f"The number {num} is valid. ")