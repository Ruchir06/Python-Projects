# def happy_birthday():
#     print("Happy Birthday to you")
#     print("Happy Birthday to you")
#     print("My family member")

# no_of_times = int(input("Enter how many times you want to sing the song: "))
# i=0

# while(i < no_of_times):
#     happy_birthday()
#     print(" ")
#     i += 1


# def favourite_pokemon(name, pokemon_type):
#     print(f"My favourite pokemon is {name}")
#     print(f"This pokemon is a {pokemon_type} type pokemon")

# favourite_pokemon("charizard", "fire")

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Joe", 1000, "2022/02/02")

# def net_price(list_price, discount, tax): 
#     return list_price * (1 - discount) * (1 + tax)
# print(net_price(500, 0.10, 0.10))

# def net_price(list_price, tax, discount = 0.05): 
#     return list_price * (1 - discount) * (1 + tax)
# print(net_price(500, 0.10))

# import time
# def count(start, end):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("DONE")

# (count(0,10))

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# # hello("Hello", "Mr.", "Spongebob", "Squarepants")
# hello("Hello", title = "Mr.", last = "Squarepants", first = "Spongebob")

def get_phone(country_code, area, first, last):
    return f"+{country_code} {area}{first}{last}"

phone_number = get_phone(country_code= 91, area= 9, first= 9109, last= 78206)
print(phone_number)