capitals = {
            "USA" : "Washington DC", 
            "India" : "New Delhi", 
            "Sri Lanka" : "Colombo", 
            }

# print(dir(capitals))

# print(capitals.get("UA"))

# if capitals.get("Sri Lanka"):
#     print("The capital exists")
# else:
#     print("The capital doesn't exist")

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "Detroit"})

# capitals.pop("India")

# capitals.clear()
# capitals.popitem()

# print(capitals.keys())
# print(capitals)
val = capitals.values()
for cities in val:
    print(cities)