menu = {
        "pizza" : 3.00,
        "burger" : 2.00,
        "nachos" : 2.00,
        "popcorn" : 3.00
}

cart = []

total = 0

print("----------------MENU----------------")
for key, value in menu.items():
    print(f"{key}: {value:.2f}")

print("----------------MENU----------------")

while True: 
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)


for food in cart:
    total += menu[food]

print("\n--------- YOUR ORDER ---------")
for food in cart:
    print(food)
print(f"\nTotal: ${total:.2f}")