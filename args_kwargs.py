# def add(*args):
#     total = 0
#     for num in args: 
#         total = total + num
#     return total

# print(add(1, 2, 3, 4))

# def display_name(*names):
#     for name in names: 
#         print(name, end = " ")

# display_name("Mr.", "spongebob", "square", "pants" )

def print_address(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(address = "123 fake street",
              city = "Gurgaon", 
              state = "Haryana", 
              country = "India")